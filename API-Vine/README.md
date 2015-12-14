# Vine-API
![logo](http://humandynamics.sdsu.edu/images/HDMA_Logo.png)
##Retrieve video and user data from Vine using third-party Vine API 
######*Project conducted by*: San Diego State University
######*Report prepared by*: Ardeshir Beheshti (Department of Geography, San Diego State University)
#### Abstract
The following report is to explain the Vine API, which introduces and allows developers to work with the Vine database to obtain information (location, username, subtext, etc.) about the specific uploaded content. From using and understanding the API information to using API methods to acquire user information/data. 

#### 1.	What is Vine?
Vine is a mobile short-clip video sharing service which is giving the users an opportunity to record and share a six-second-long looping video clip. The general users of this application use it as a form of entertainment for their viewers (or followers). This app is not limited to just an entertainment service. https://en.wikipedia.org/wiki/Vine_(service)

#### 2.	What is Vine API?
When a registered user publishes a video to Vine, it will appear in their profile and in the timelines of their followers. Videos can also be posted to Twitter and Facebook. The Vine API allows users to retrieve data from the service, including popular videos, user data, a user's timeline, videos matching a given tag, individual posts, and notifications. 

#### 3.	Vine API Key
Since Vine does not have their own API online, third-party users create their own API for searching the Vine database. Once you create an account, you can access all of the APIs along with their keys since these are not registered by the company. In this specific circumstance, you need to use this since the company did not provide their own API. These third-party APIs can be found on: https://market.mashape.com/dashboard

#### 4.	Using Unirest (third-party API) 
Unirest is a simplified, lightweight HTTP client library application. This application can be access Vine data base through Python 2.7 but nothing higher. Unirest can also be downloaded: https://pypi.python.org/pypi/Unirest/ 

#### 5.	Market.mashape APIs
Next, you go to https://market.mashape.com/community/vine-app giving you specific command strings to use on Unirest to find information on Vine users. Marketplace has codes written already: Curl, Java, Node, PHP, Pyhton, C#, Ruby, and .Net.

#### 6. These next few sets of code are to show examples of the appropriate commands needed to get information. The first is just to show a user logging in:

* The first commmand is a typical user login
![](http://imgur.com/YlgBPtF.jpg)


* Now by using the Get command, we are able to track something like popular vines in the past 24 hours. Again, this is just another example of tagging and finding popular vines giving their location, description, longitude & latitude, username, and other social media websites it has been shared with.
![](http://imgur.com/kfQ5baN.jpg)![](http://imgur.com/sIkctlC.jpg)



