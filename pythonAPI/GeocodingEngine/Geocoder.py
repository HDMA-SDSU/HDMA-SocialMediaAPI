import math
import re   
import os
   
CITIES_FILE = "uscities.txt"
   
   
'''
	CityGeocoder provides a way to geocode city names.
	It uses the GeoNames database.
'''
class CityGeocoder(dict):

	def __init__(self, items = None, file=CITIES_FILE):        
		super(CityGeocoder, self).__init__()

		self._loadFile(file)


	def _loadFile(self, file):
		COL_CITY = 0
		COL_ALT_NAMES = 1
		COL_LAT = 2
		COL_LON = 3

		cwd = os.path.dirname(__file__)
		path = cwd + '\\' + file 

		f = open(path)
		lines = f.read().split('\n')
						  
		for line in lines:
			cols = line.split('\t')
			names = [cols[COL_CITY]]
			names.extend(cols[COL_ALT_NAMES].split(','))

			for name in names:
				key = name.lower().strip()
				#val = { 'name': cols[COL_CITY], 'coords': (float(cols[COL_LAT]), float(cols[COL_LON])) }
				val = (cols[COL_CITY], (float(cols[COL_LAT]), float(cols[COL_LON]))) 
				self.__setitem__(key, val)           
            

	def lookup(self, location):
		'''
		lookup(location):
			Returns tuple of the city name and the coordinates.
			If the location can't be located, returns ('None', (0.0, 0.0)
		'''

		noplace = (None, (None, None))

		if not location or type(location) is not str:
			return noplace

		loc = location.lower().strip()

		if loc in self:
			return self.__getitem__(loc)

		token = loc.split(",")[0].strip()
		if token in self:
			return self.__getitem__(token)

		firstWord = re.findall(r'\w+', loc)[0]
		if firstWord in self:
			return self.__getitem__(firstWord)

		return noplace
       
	   
'''
	AddressGeocoder provides a API for geocoding address information.
	Note: Currently, this is just a wrapper for the geopy geocoders,
	but we can use the same API when our own custom geocoder is set up.
'''	
class AddressGeocoder(object):
		
		def __init__(self, username=None, password=None, geocoderName="GEOCODERDOTUS"): 			
		
			import geopy
		
			geocoderName = geocoderName.upper()
			
			if geocoderName == "GEOCODERDOTUS":
				if username and password:
					#self._geocoder = geopy.geocoders.GeocoderDotUS(username, password)
					#NOTE: I don't believe geopy handles Geocoder.US usernames and passwords
					#properly, so just calling without these for now...
					self._geocoder = geopy.geocoders.GeocoderDotUS()
				else:
					self._geocoder = geopy.geocoders.GeocoderDotUS()
			else:
				self._geocoder = geopy.geocoders.GoogleV3()
		
		def lookup(self, location):
			noplace = (None, (None, None))
		
			#different geocoder return different values
			#some return a list of possible matches, other
			#just return the best match
			coded = self._geocoder.geocode(location, exactly_one=False)  
			if coded and coded is list:
				place, (lat, lng) = coded[0]
				if place and lat and lng:
					return (place, (lat, lng))
				else:
					return noplace
			elif coded:
				place, (lat, lng) = coded
				if place and lat and lng:
					return (place, (lat, lng))
				else:
					return noplace
			
			return noplace
		
