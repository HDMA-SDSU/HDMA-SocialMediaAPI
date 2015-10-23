![logo](http://humandynamics.sdsu.edu/images/HDMA_Logo.png)
##Retrieve Photo Data from Flickr Using Flickr API - NIH Proposal for Food Environment
######*Project conducted by*: San Diego State University
######*Report prepared by*: Yi-ting Chuang (Department of Geography, San Diego State University)
#### Abstract
This technical note introduces how to retrieve food photos at Downtown San Diego from Flickr by using Flickr API. This notes searched photos by setting longitude, latitude and radius arguments. 

 
#### 1.	What is Flickr?
Flickr is an image hosting and video hosting website, and web services. Users can not only share and embed personal photographs but also effectively attend an online community. The service is widely used by photo researchers and by bloggers to host images that they embed in blogs and social media. (http://en.wikipedia.org/wiki/Flickr)
#### 2.	What is Flickr API?
Registered users can search photos and related information according to different arguments by using Flickr API.
#### 3.	Does the API need a key?
Yes, before utilizing Flickr API, developers need to get an access key and secret code for calling methods of Flickr API. Go here: https://www.youtube.com/watch?v=Lq1XRx6dsDU.
#### 4.	How to find photos for specific geographic areas? (e.g. Downtown San Diego)
flickr.photos.search() method allows users to search photos taken at specific locations. Parameters in this method include: 
Tags: A comma-delimited list of tags. Photos with one or more of the tags listed will be returned. You can exclude results that match a term by prepending it with a - character. (e.g. Food)
Lon: A valid longitude, in decimal format, for doing radial geo queries. (e.g. -117.161)
Lat: A valid latitude, in decimal format, for doing radial geo queries. (e.g. 32.726)
Radius: A valid radius used for geo queries, greater than zero and less than 20 miles (or 32 kilometers), for use with point-based geo queries. The default value is 5 (km).
Other parameters: https://www.flickr.com/services/api/flickr.photos.search.html
#### 5.	The following is an example of photos with “food” tag at Downtown San Diego (latitude: 32.715754; longitude: -117.161093) with 5 kilometers radius.

```
Photo Data:
"photo": [
      { "id": "16002140699", "owner": "31911001@N00", "secret": "262c519825", "server": "8649", "farm": 9, "title": "Chilaquiles WTF", "ispublic": 1, "isfriend": 0, "isfamily": 0 },
      { "id": "15241138255", "owner": "15474023@N03", "secret": "960b0d8a36", "server": "5552", "farm": 6, "title": "IMG_3408", "ispublic": 1, "isfriend": 0, "isfamily": 0 },
      { "id": "15128197056", "owner": "65172614@N06", "secret": "f6d8f31795", "server": "3850", "farm": 4, "title": "Croque monsieur", "ispublic": 1, "isfriend": 0, "isfamily": 0 },
      { "id": "14863357020", "owner": "34128007@N04", "secret": "ba4e3d20d1", "server": "3879", "farm": 4, "title": "Fruit Tart", "ispublic": 1, "isfriend": 0, "isfamily": 0 },
      { "id": "14813732619", "owner": "7183730@N06", "secret": "80a732dac5", "server": "5552", "farm": 6, "title": "Scallop omelette", "ispublic": 1, "isfriend": 0, "isfamily": 0 },
      { "id": "14813823548", "owner": "7183730@N06", "secret": "984a519a95", "server": "3871", "farm": 4, "title": "", "ispublic": 1, "isfriend": 0, "isfamily": 0 }
```

Flickr photo format: https://farm{farm-id}.staticflickr.com/{server-id}/{id}_{secret}.jpg


This note only utilizes flickr.photos.search() method to search photos. For more information (e.g. date, place id, and size) of photos, go to [https://www.flickr.com/services/api/](https://www.flickr.com/services/api/).

####Demo site: http://vision.sdsu.edu/ychuang/Flickr_InstagramAPI/socialMedia_API.html
