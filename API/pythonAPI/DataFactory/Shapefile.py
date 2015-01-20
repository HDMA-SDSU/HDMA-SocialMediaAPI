

class Shapefile(object):
	
	def __init__(self, fileName):
		import fiona
		
		self._source = fiona.open(fileName, "r")
		self._features = list(self._source)
		
		
	def getBounds(self):
		return self._source.bounds
	
	
	def getFeatures(self):
		return self._features
		
	def filterByProperty(self, 
		#there's a SetAttributeFilter in OGR...use that?
		pass
		
	
	def filterByPolygon(self, properties):
		#??
		pass
	
		
	def saveAsSHP(self, outName):
		output = fiona.open(outName, 'w', **self._source.meta)
		outpu.writerecords(list(self._features))
		
		
	def saveAsGeoJSON(self, outName):
		import json
		
		featureCollection = dict(type="FeatureCollection", features=self._features, crs={})
		
		out = open(outName, "w")
		out.write(json.dumps(featureCollection))

	@classmethod
	def saveGeoJSONFeatures(features):
		pass
		
