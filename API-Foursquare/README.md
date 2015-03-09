![logo](http://humandynamics.sdsu.edu/images/HDMA_Logo.png)
######*Project conducted by*: San Diego State University
######*Content prepared by*: Jiue-An (Jay) Yang @ San Diego State University

---

## Working with the Foursquare API (using Python)

---

#### Introduction
Welcome to the section about the Foursquare API.
Lets start with the Foursquare API 101, and then you can explore more about using the API by reading our technical note or check out our examples.

---

#### Foursquare API 101

##### 1. What is Foursquare ?

>[Foursquare](https://foursquare.com/) is a local search and discovery service mobile app which provides a personalised local search experience for its users. By taking into account the places a user goes, the things they have told the app that they like, and the other users whose advice they trust, Foursquare aims to provide highly personalised recommendations of the best places to go around a user's current location.

##### 2. What is Foursquare API ?

>The [Foursquare API](https://developer.foursquare.com/start) (Application Programming Interface) allows developer to connect to the Foursquare database.  Developers can retrieve users and venues information or interact with Foursquare users and merchants.

##### 3. Is the Foursquare Free ?

>**Yes**, using the API is free.  However, you will need to sign-up for a Foursquare account and then register your account to the [Foursquare for Developer](https://developer.foursquare.com/) to create your application. The registered application will grant you API keys that you need to interact with the Foursquare database.

##### 4. To search for Foursquare Venues, what parameters I can use ?

>The Search Venues method allow you to use parameters such as *search center* (latitude & longitude), *radius*, *venue name* ...etc.

##### 5. What does the response looks like ?

>Foursquare API responses are in JSON (JavaScript Object Notation) format.  Following is an example of one Starbucks venue that is located at the San Diego State University.

```json
{
    "venues": [
        {
            "hasMenu": true,
            "verified": false,
            "name": "Starbucks",
            "referralId": "v-1423476221",
            "url": "http://www.starbucks.com",
            "menu": {
                "url": "https://foursquare.com/v/starbucks/4b832dc7f964a52000fc30e3/menu",
                "mobileUrl": "https://foursquare.com/v/4b832dc7f964a52000fc30e3/device_menu",
                "type": "Menu",
                "anchor": "View Menu",
                "label": "Menu"
            },
            "contact": {
                "phone": "6195947733",
                "twitter": "starbucks",
                "formattedPhone": "(619) 594-7733"
            },
            "location": {
                "distance": 202,
                "city": "San Diego",
                "cc": "US",
                "country": "United States",
                "postalCode": "92115",
                "state": "CA",
                "formattedAddress": [
                    "5500 Campanile Dr",
                    "San Diego, CA 92115",
                    "United States"
                ],
                "address": "5500 Campanile Dr",
                "lat": 32.77626,
                "lng": -117.07404
            },
            "stats": {
                "tipCount": 5,
                "checkinsCount": 1152,
                "usersCount": 338
            },
            "id": "4b832dc7f964a52000fc30e3",
            "categories": [
                {
                    "pluralName": "Coffee Shops",
                    "primary": true,
                    "name": "Coffee Shop",
                    "shortName": "Coffee Shop",
                    "id": "4bf58dd8d48988d1e0931735",
                    "icon": {
                        "prefix": "https://ss3.4sqi.net/img/categories_v2/food/coffeeshop_",
                        "suffix": ".png"
                    }
                }
            ]
        }
    ]
}
```


--- 

#### Getting Started !

+ Kick start and learn how to use the API by follow our *[technical note](https://github.com/HDMA-SDSU/HDMA-SocialMediaAPI/tree/dev/API-Foursquare/Tech_Document)*
+ Or check out our *[examples](https://github.com/HDMA-SDSU/HDMA-SocialMediaAPI/tree/dev/API-Foursquare/Example)* of a web search interface and a python script
+ For detailed methods and documentation of the Foursquare API, please go to the official [Foursquare for Developer](https://developer.foursquare.com/) page

---

#### Folder Structure
- Examples
	1. Web Search Interface Example
	2. Python Script Example
- Technical Document
	1. Technical Note on Working with Foursquare API (in .docx format)