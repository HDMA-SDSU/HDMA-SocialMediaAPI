
<img src='http://humandynamics.sdsu.edu/images/HDMA_Logo.png' width="60%"  />

##Google Places API
######*Project conducted by*: San Diego State University
######*Report prepared by*: Chin-Te (Calvin) Jung (Department of Geography, San Diego State University)

## Abstract

This report introduces the Google Places API, which allows developer to connect to the Google Places database for retrieval of place features (including more than 100 million businesses and points of interest that are updated frequently).  This report covers details about using the API, from getting started with applying the API keys to using the API method and retrieving data.   The data retrieved from Google Places with the API has potential to be used for mapping and analyzing accessibility to food.

This report covers the following items:
- Introduction of Google Places
- Apply for Google Places API key
- Import Google Places API into your Web applications
- Search for a Starbucks venue within 1000 meters radius of  a location.




## Website
https://developers.google.com/places/javascript/


## Introduction
Google Places is the database which collects more than 100 million businesses and points of interest that are updated frequently through owner-verified listings and user-moderated contributions. The Google Places API is the application programming interface (API) developed by Google which we can use multi programming languages, including JavaScript, Java, or Object C, to query the database. This report only focuses on JavaScript (JS) programming language and uses JS to demonstrate how to query Google Places. 

The Google Places API for JS provides the following ways to conduct a search.
- **getDetail**
retrieves details about the place identified by the given placeId. 
- **nearbySearch**
retrieves a list of places in a given area.
- **radarSearch**
similar to the nearBySearch but only include up to 200 places which are identifies only by their geographic coordinates and place_id. 
- **textSearch**
similar to the nearBySearch but based on the comparison of keywords. If bounds or location+radius is provided in the search criteria, the reulsts will not restrict the results to places inside the area, only bias the response towards results near it. 

The information about a place can be retrieved in a search result, which is in JSON (JavaScript Object Notation) format. The information includes name, coordinates, description, addresses, phone number, websites, time zone, photos, price level (from free to very expensive), user reviews, ratings (from 1 to 5 stars), and types (such as restaurant or establishment). 



## The Google Places API Key

To get started, the first thing to do is to get an API key for Google Places. The API key uses Google Maps API Key. If you already have Google Maps API key, you can skip this part. If you don’t have or don’t know how to get one, please follow these steps.
1.	Go to Google Developers Console (https://console.developers.google.com)
2.	Create or select a project
3.	Activate the Google Maps JavaScript API under APIs
 

4.	Get an API key by switching to credentials under APIs & auth. Create a new Browser key.
 
5.	Give a name for the browser key and press Create button
6.	You will get an API key. 
7.	Please  remember that the limit for free usage of Google Places API is 150,000 request per 24 hour period. 



## Import Goolge Places API into your Web applications

1.	After your get the Google API key, you need to import Google Places API into your Web application with the API key.
    ```sh
    <script type="text/javascript" src="https://maps.googleapis.com/maps/api/js?key=AIzaSyAqd6BFSfKhHPiGaNUXnSt6jAzQ9q_3DyU&libraries=places"></script>
    ```  
    
2.	You need to init a Google Maps object first to have a google Place object.
    ```sh
    var map=new google.maps.Map(document.getElementById("domID_MAP")); 
    var googlePlace=new google.maps.places.PlacesService(map)
    ```  
3.	Make a query request to Google Places. For example, if we would like to search Startbucks nearby a certain location with latitude and longitude. We can use “nearbySearch” function to do the query. The results will be responded in the callback function. Then you can continue to parse results and visualize them. 
     ```sh
    googlePlace.nearbySearch({
    	location: new google.maps.LatLng(lat, long),
    	radius: 100  //unit: meter
    	types: [“restaurant”]   //categories
    	name: “starbucks”  //query name
    }, 
    function(results){
    	//callback function
    
    
    });
    ```  

4.	Please see more details in [the demo site](http://vision.sdsu.edu/ychuang/Flickr_InstagramAPI/socialMedia_API.html]) or see the codes in the [Github](https://github.com/HDMA-SDSU/HDMA-SocialMediaAPI/blob/dev/API-GooglePlaces/Example/index.html).






