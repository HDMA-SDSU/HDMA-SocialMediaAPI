
import foursquare

my_Client_id = 'your Client ID'
my_Client_secret = 'your Client Secret'

client = foursquare.Foursquare(client_id = my_Client_id, 
							   client_secret = my_Client_secret)

client.venues.search(params={'ll': '32.775278, -117.072222',
                                             'query': 'starbucks',
                                             'radius': 1000})


