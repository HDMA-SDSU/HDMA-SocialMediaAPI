# -*- coding: utf-8 -*-
"""
This code is prototype and has been configured for my account.
It download the tweets that has some location shared in it.

You need a token to run the script.
Steps to get a token.
    1) Goto https://developers.facebook.com/apps/
    2) Click on Tools & Support
    3) Click on Graph API Explorer
    4) Copy Access Token
"""
__author__ = "Sagar N Jha <sjha1@kent.edu>, Xinyue Ye <xye5@kent.edu>"

import facebook
import requests

def Statuses():
    """
    The token might get expired and use your own token.
    It will fetch status shared by you with some location information
    """
token = 'get your own token'

user = 'me'
graph = facebook.GraphAPI(token)
profile = graph.get_object(user)
status = graph.get_connections(profile['id'], 'statuses')

# Wrap this block in a while loop so we can keep paginating requests until finished.
print ("Location",19*' ' ,"Latitude",18 * ' ',"Longitude",15 *" " ,"Status")
print ("-" * 122)
while True:
    try:
        # Perform some action on each post in the collection we receive from facebook.
        
        for item in status['data']:
            
            if "place" in item.keys():
                
                if "city" in item['place']['location']:
        
                    city = item['place']['location']['city']
                    lat  = item['place']['location']['latitude']
                    longi = item['place']['location']['longitude']

                    city = city + ' ' *(25-len(city))
                    lat = str(lat) + ' ' *(25-len(str(lat)))
                    longi = str(longi) + ' ' *(25-len(str(longi)))

                    if "message" in item.keys():
                        print (city,"|",lat,"|",longi,item['message'])
                    else:
                        print (city,"|",lat,"|",longi)
                        
                    print ("-" * 122)

        # Attempt to make a request to the next page of data, if it exists.
        status = requests.get(status['paging']['next']).json()
    except KeyError:
        # Break loop if no page is left to display items.
        break
