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

```
GET graph.facebook.com
	/me/photos
```

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
 POST graph.facebook.com
	/{user-id}/feed?
    message={message}&access_token={access-token}
```
* *HTTP DELETE*: Also used to delete data in Facebook social graph. The JavaScript clients are not supported; those clients have to issue a *POST* request to delete an object.
```
POST graph.facebook.com
	/{comment-id}?method=delete
```
#### 2. Graph API Explorer
In this section, the basic interface of Facebook graph API explorer and its main functions will be introduced.
* **a) The Web-based Interface of Graph API Explorer ( https://developers.facebook.com/tools/explorer/ )**

The easiest tool for using the Graph API is the Graph API Explorer; for using it a registered Facebook account is required.
* **b) Get the Access Token**

*When someone connects with an app using Facebook Login, the app will be able to obtain an access token which provides temporary, secure access to Facebook APIs. —from Facebook developers website*

You will automatically get an access token with default data access permissions when you open the Graph API Explorer.By default Facebook only allows you to retrieve the basic information. For testing you can push the "Get Access Token" button and grant the other data access permissions in the pop-up window.

* **c) Make the Requests**

The HTTP requests can be submitted by clicking the "Submit" button on the *Graph API Explorer* webpage. You can select different requests (GET, POST, or DELETE) and input the search target (i.e. a node-id) to explore the query data. In this document we will only focus on how to read (GET) the data out of Facebook's social graph. 

* **d) GET a “Zoo”!**

The HTTP GET request can be use to retrieve the data from **nodes** (such as a User, a Photo, a Page, or a Comment). For example, if you want to know the information about the San Diego Zoo, you need to input the node-id ‘28896772146’ or its name ‘SanDiegoZoo’ into the query field and push the submit button. The result will come up immediately with a JSON string.

As can be seen, the detail information of the San Diego Zoo will be included in the JSON string as JSON objects, those objects are the **fields** of the ‘SanDiegoZoo’ **node**. You can also use your web browser and type in http://graph.facebook.com/SanDiegoZoo to get the same result. Here the access token is not required because the SanDiegoZoo is a public place in Facebook. 

If the **node** has a location **fields**, you will find the location information such as address, zip code, or geographical coordinates inside the location object if provided. You can append a search string like ‘?fields =location’ after the node-id or name if you don’t want to see other information but the location information. You can also make a query for multiple fields as well.

* **e) Graph API Search**

All public objects can be searched in the Facebook social graph. When using the Graph API Search, the App or user access tokens is required for all search Graph API calls.  
For example, if you want to search coffee shops over the place objects in the social graph, you can use the GET request like:
```
https://graph.facebook.com/
			search?q=coffee&type=place
			&access_token={access-token}
```

This search can be narrowed to a specific location and searching radius by adding the **center** (with latitude and longitude) parameter and a optioanl **distance** parameter. The distance is messured in meters.
```
https://graph.facebook.com/
			search?q=coffee&type=place
			&center=37.76,-122.427&distance=1000
			&access_token={access-token}
```
* **f)** You can also narrow the search by adding the **fields**  parameter. For example, if you only want to show the name and the location information, you will need to append a string like ‘fields=name,location’ to the search string and then all other information will be hidden (see figure 10). Note that the subfields are not supported by location which means you can not extract the subfield information (i.e. latitude and longitude) seperately from the location **fields**.

#### 3. *Facebook SDKs*
Facebook provides official SDKs for iOS, Android, Unity, JavaScript and PHP. There are also many third-party SDKs for other languages such as Python-sdk. A python example may look like:
```
import facebook
# initialize the graphAPI object
graph = facebook.GraphAPI(access_token='your_token', version='2.2')
# get the information of San Diego Zoo by input the Node ID
sandiegozoo = graph.get_object(id=28896772146')
# get the checkin number of San Diego Zoo from the output data
print(sandiegozoo['checkins'])
```

#####For more information please go https://developers.facebook.com.
#####Demo Site: http://vision.sdsu.edu/ychuang/Flickr_InstagramAPI/demoFB.html
