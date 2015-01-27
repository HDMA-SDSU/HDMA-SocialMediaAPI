from pymongo import MongoClient

class GeoMongoClient:
	MULTIGEOMETRY = ("MULTILINESTRING", "MULTIPOLYGON")

	def __init__(self, dbName, collectionName, createNew=True):
		try: 
			self._connection = MongoClient()
		except Exception, e:
			raise e
		
		if dbName not in self._connection.database_names():
			raise Exception("Error: Database not found: %s." % dbName)
			
		self._db = self._connection[dbName]	
		
		if not createNew and collectionName not in self._db.collection_names():
			raise Exception("Error: Collection not found: %s." % collectionName)
		
		self._collection = self._db[collectionName]
		
		#make sure spatial index is created
		self._collection.ensure_index([("geometry", "2dsphere")])
	
	
	def _combineMultiGeometry(self, docs):
		'''
			Private method that combines multigeometry by looking at the "groupId"  
			property.  Since MongoDB does not recognize the MultiPolygon and MultiLineString
			GeoJSON types, these must be split up when inserted and re-combined when 
			queried.
		'''
		
		results = []
		doneGroups = []
		
		for doc in docs:
			if 'groupId' in doc:
				if doc['groupId'] not in doneGroups:
					groupResults = self._collection.find( { 'groupId': doc['groupId'] } )
					
					group = { 'type': 'Feature', 'properties': doc['properties'] }
					group['geometry'] = { 'type': 'MultiPolygon' if doc['geometry']['type'].upper() == 'POLYGON' else 'MultiLineString' }
					
					group['geometry']['coordinates'] = [ g['geometry']['coordinates'] for g in groupResults ]
					
					doneGroups.append(doc['groupId'])
					results.append(group)
			else: 
				results.append(doc)
		
		return results
			
		
	def withinPointBuffer(self, center, radiusMiles):
		'''
			Returns all features that are within the region defined by the 
			center point ("center") and the radius ("radiusMiles").
		'''
		#convert miles to meters
		radiusMeters = radiusMiles * 1609.34
		
		
		query = { 'geometry': { '$near' : { '$geometry' : { 'type': 'Point', 'coordinates': center }, '$maxDistance' : radiusMeters } } }
		results = self._collection.find(query, {"_id" : 0})
		results = self._combineMultiGeometry(results)		
		
		return [result for result in results]
	
	
	def withinBoundingBox(self, lowerLeft, upperRight):
		'''
			Returns all features within the bounding box defined by the "lowerLeft" and 
			"upperRight" parameters.  The function expects each of these parameters to 
			be a point that defines the lower left and upper right corners of the bounding box.
		'''
	
		polygon = [ [ lowerLeft[0], lowerLeft[1] ], [ lowerLeft[0], upperRight[1] ],
					[ upperRight[0], upperRight[1] ], [ upperRight[0], lowerLeft[1] ], 
					[ lowerLeft[0], lowerLeft[1] ] ]
		
		query = { 'geometry': { '$geoWithin': { '$geometry': { 'type': 'Polygon', 'coordinates': [ polygon ] } } } }
		results = self._collection.find(query, {"_id" : 0})
		results = self._combineMultiGeometry(results)
		
		return [result for result in results]
		
		
	def withinPolygon(self, polygon):
		'''
			Returns all features that are within the "polygon" parameter.
		'''
	
		query = { 'geometry': { '$geoWithin': { '$geometry': { 'type': 'Polygon', 'coordinates': [ polygon ] } } } }
		results = self._collection.find(query, {"_id" : 0})
		results = self._combineMultiGeometry(results)
		
		return [result for result in results]		
	
	
	def intersectsPolygon(self, polygon):
		'''
			Returns all features that either intersect OR are within the "polygon" parameter.
		'''
	
		query = { 'geometry': { '$geoIntersects': { '$geometry': { 'type': 'Polygon', 'coordinates': [ polygon ] } } } }
		results = self._collection.find(query, {"_id" : 0})
		results = self._combineMultiGeometry(results)
		
		return [result for result in results]
	
	
	def intersectsLine(self, line):
		'''
			Returns all features that intersect with the "line" parameter.
		'''
	
		query = { 'geometry': { '$geoIntersects': { '$geometry': { 'type': 'LineString', 'coordinates': line } } } }
		results = self._collection.find(query, {"_id" : 0})
		results = self._combineMultiGeometry(results)
		
		return [result for result in results]
		
	
	
	
	def _convertIfNumeric(self, val):
		'''
			Checks whether the passed parameter "val" can be converted to an integer
			or float.  If so, it returns the converted value.  Otherwise, it returns the
			original parameter.
		'''
		
		def isFloat(string):
			try:
				float(string)
				return True
			except:
				return False

		if hasattr(val, 'isdigit') and val.isdigit():
			return int(val)
		elif isFloat(val):
			return float(val)
		
		return val
	
	
	def _explodeMultiGeometry(self, geoJson):
		'''
			Private method that explodes multigeometry by before inserting into the database.  
			Since MongoDB does not recognize the MultiPolygon and MultiLineString
			GeoJSON types, these must be split up when inserted and re-combined when 
			queried.
		'''
		if not self._collection:
			return []
			
		if geoJson['geometry']['type'].upper() not in ('MULTIPOLYGON', 'MULTILINESTRING'):
			return geoJson
			
		#get the next groupId available...
		groupId = len(self._collection.find().distinct("groupId")) + 1
		
		result = []
		
		for coords in geoJson['geometry']['coordinates']:
			item = {}
			item['type'] = geoJson['type']
			item['properties'] = geoJson['properties']
			item['groupId'] = groupId
			item['geometry'] = { "type": "Polygon", "coordinates": coords }
			
			result.append(item)
		
		return result	

		
	def saveFeature(self, geoJson):
		'''
			Inserts the "geoJson" parameter into the current collection.  
		'''

		#convert all strings to their numerical values (if applicable)
		for prop in geoJson['properties']:
			geoJson['properties'][prop] = self._convertIfNumeric(geoJson['properties'][prop])
					
			
		#if this feature is a MultiPolygon, explode it into a group of Polygons
		if geoJson['geometry']['type'].upper() in ('MULTIPOLYGON', 'MULTILINESTRING'):
			multi = self._explodeMultiGeometry(geoJson)
			
			for item in multi:
				self._collection.insert(item)

		else: 
			self._collection.insert(geoJson)
			
	def saveFeatures(self, geoJsonList):
		'''
			Inserts each element of the "geoJsonList" parameter into the current collection.
		'''
		
		for geoJson in geoJsonList:
			self.saveFeature(geoJson)
	

	def find(self, query, removeObjectID=False):
		'''
			Performs a query on the current collection.  Uses standard MongoDB query syntax.
		'''
		
		if type(query) is not dict:
			raise Exception("Query must be a dictionary (ie, JSON).")
			
		exclude = {"_id" : 0} if removeObjectID else None
		
		return [ item for item in self._collection.find(args, fields=exclude) ]
		
	def update(self, document):
		'''
			Updates the current collection with the passed "document" parameter.
			Note: An Object ID field must be included in the "document" object, otherwise
			a new record will be created in the collection.
		'''
		
		self._collection.save(document)
		
	
			