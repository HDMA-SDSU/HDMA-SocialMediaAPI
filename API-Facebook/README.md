![logo](http://humandynamics.sdsu.edu/images/HDMA_Logo.png)
##Introduction to Facebook Graph API
######*Project conducted by*: San Diego State University
######*Report prepared by*: Chih-Yuan Chen
#### Abstract
This technical document will introduce the **Facebook Graph API** and demonstrate how to use the ***Graph API Explorer***, the easiest tool for testing the API. Facebook provides the Graph API for retrieving data in and out of its social graph. This document will start from the basic concepts of Graph API and make a brief introduction of its key elements, the three different types of **HTTP requests**, and the user access token. The second part of this document will demonstrate an example about how to use the ***Graph API Explorer*** to get information from San Diego Zoo facebook page. In addition, a summary of the official and third-party SDKs and a simple python code example are provided. 

#### 1.	What is Graph API?
*The Graph API is the primary way to get data in and out of Facebook's social graph. It's a low-level HTTP-based API that you can use to query data, post new stories, upload photos and a variety of other tasks that an app might need to do.
… The APIs are composed of nodes (such as a User, a Photo, a Page, a Comment), edges (such as a Page’s Photos, or a Photo’s Comments), and fields (such as the birthday of a User, or the name of a Page).
—from Facebook developers website*

Currently, the latest version of the Graph API is v2.2.

There are three different kinds of requests which Graph API provides:
* *HTTP GET*: The most widely used request in the Graph API used to read all the **nodes and edges**. For example if you want to read all your photos you can do the request below:

```GET graph.facebook.com/me/photos```

Some request will need the access token to make the API calls. If you don’t have it you may get the error message like:
```
{
   "error": {
      "message": "An active access token must be used to query information about the current user.",
      "type": "OAuthException",
      "code": 2500
   	}
}
```
* *HTTP GET*: The POST request is used to create, update, and delete data in the social graph. For example if you want to publish a post on behalf of someone, you can do:
```
  POST graph.facebook.com/{user-id}/feed?message={message}&access_token={access-token}
```
* *HTTP DELETE*: Also used to delete data in Facebook social graph. The JavaScript clients are not supported; those clients have to issue a *POST* request to delete an object.
```
POST graph.facebook.com/{comment-id}?method=delete
```
#### 2. Graph API Explorer
In this section, the basic interface of Facebook graph API explorer and its main functions will be introduced.
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
