'''
This script will import features from a shapefile into MongoDB as GeoJSON objects.
The user must specify both the shapefile to be imported and the name of the collection
where the GeoJSON output will be stored.

Usage: 	python importShapefile.py [Shapefile Path] [Collection Name]

EX: 	python importShapefile.py counties.shp GeoJSONCounties


NOTE: Any feature that contains multiple polygons (ie, a MultiPolygon) will be split up, 
since MongoDB does not allow for MultiPolygons.  For instance, a MultiPolygon containing 
three polygons will be split into three separate GeoJSON objects.  These objects are 
given an extra property called "groupId" that links these objects together. 
'''


import traceback
import ogr, json
from pymongo import MongoClient


DATABASE_NAME = "test"
collection = None


# This function converts a string to an integer or float (where possible)
def convertIfNumeric(val):
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
	
	
def makePolygonValid(geometry):
	from shapely.geometry import mapping, shape
	dirty = shape(geometry)
	clean = dirty.buffer(0.0)
	return mapping(clean)	
	
	
# This function takes a MultiPolygon GeoJSON object as an input
# and splits it into a list of separate Polygons.
def explodeMultiPolygon(geoJson):
	if not collection:
		return []
		
	#get the next groupId available...
	groupId = len(collection.find().distinct("groupId")) + 1
	
	result = []
	
	for coords in geoJson['geometry']['coordinates']:
		item = {}
		item['type'] = geoJson['type']
		item['properties'] = geoJson['properties']
		item['groupId'] = groupId
		item['geometry'] = { "type": "Polygon", "coordinates": coords }
		
		result.append(item)
	
	return result
	
	
def main(fileName, collectionName, dbName=DATABASE_NAME):
	try: 
		#set up database connection
		conn = MongoClient()
		global collection
		collection = conn[dbName][collectionName]
		
		#make sure the spatial index is created for GeoJSON
		collection.ensure_index([("geometry", "2dsphere")])
	
		#open shapefile
		shp = ogr.Open(fileName)
		layer = shp.GetLayer(0)
		
		#keep track of successes and failures
		successCount = 0
		featureCount = 0
		failures = []
		
		for fid in xrange(layer.GetFeatureCount()):
			try:
				feature = layer.GetFeature(fid)
				geoJson = json.loads(feature.ExportToJson())
				
				#convert all strings to their numerical values (if applicable)
				for prop in geoJson['properties']:
					geoJson['properties'][prop] = convertIfNumeric(geoJson['properties'][prop])
					
				#geoJson['properties']["center"] = [ float(geoJson['properties']['INTPTLON']), float(geoJson['properties']['INTPTLAT']) ]
				
				if not feature.geometry().IsValid():
					print 'yo'
					geoJson['geometry'] = makePolygonValid(geoJson['geometry'])
					print 'no'
				
				#if this feature is a MultiPolygon, explode it into a group of Polygons
				if geoJson['geometry']['type'].upper() == "MULTIPOLYGON":
					multi = explodeMultiPolygon(geoJson)
					
					for item in multi:
						collection.insert(item)
						featureCount += 1
						
				else:
					if 'id' in geoJson:
						del geoJson['id']
					
					collection.insert(geoJson)
					featureCount += 1
					
				successCount += 1
				
				if successCount % 250 == 0:
					print "Imported %d features!" % (successCount)
				
			except Exception, e:
				failures.append((fid, str(e)))
		
		conn.close()
		conn.disconnect()
		
		print "Imported %d features." % successCount
		print "Total (after multipolygons were split up): %d" % featureCount
		print "%d features could not be imported" % (len(failures))
		
		if len(failures) > 0:
			val = raw_input("Would you like to see the error details (Y/N)?")
			
			if val.upper() == "Y":

				for fid, error in failures:
					print "-" * 60
					print "Feature ID: %d" % fid
					print error[:400]
					

	except Exception, e:
		print "Critial error occured!  Aborting..."
		print str(e)
		print traceback.format_exc()
		


if __name__ == "__main__":
	import sys
	
	args = sys.argv[1:]

	if len(args) < 2:
		print "Error! Requires two arguments: 1) A shapefile, and 2) A collection name\n"
		print "EX: python %s counties.shp geoJson_counties" % (__file__)
		exit()
	
	fileName = args[0]
	collectionName = args[1]
	
	main(fileName, collectionName)
	
