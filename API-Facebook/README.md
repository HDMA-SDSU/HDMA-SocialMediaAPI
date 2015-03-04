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

* **a) The Web-based Interface of Graph API Explorer ( https://developers.facebook.com/tools/explorer/ )**
