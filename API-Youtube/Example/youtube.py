# -*- coding: utf-8 -*-
"""
Fetch youtube video urls with specific keyword mentioned.
Maximum result can be 50 only.

Get Your own access key
1) Goto https://console.developers.google.com/project
2) Create Project
3) Click on project
4) Click on APIs & auth
5) Click on Credentials
6) Copy yout API Key


"""
__author__ = "Sagar N Jha <sjha1@kent.edu>, Xinyue Ye <xye5@kent.edu>"

#import required modules
import urllib.request as urllib2
import json

part = "snippet"        #Snippet is part of the information that youtube api returns.
search = "Cop"          #Search is the keyword and you can try: prision, food,choc,baby,Polics,Cop 
maxresult = "50"        #Please dont change this 
key= "your id" # Kindly use your own key and It might get expired.

#Preparing URL to get data
#url = "https://www.googleapis.com/youtube/v3/search?locationRadius=5&part=snippet&q=food&location=(37.42307%2C-122.08427)&key=AIzaSyAVROgy5P7_tkpdnphi1-VoxPU8t27knS0"
url = "https://www.googleapis.com/youtube/v3/search?part="+part+"&q="+search+"&maxResults="+maxresult+"&key="+key

#Getting Data
json_obj = urllib2.urlopen(url)
data = json.loads(json_obj.readall().decode())
json_obj.getcode


#Publishing Data
for i in range(int(maxresult)):
    print (data['items'][i]['snippet']['title'])
    print ("https://www.youtube.com/watch?v="+data['items'][i]['id']['videoId'])
    print ("-"*120)
