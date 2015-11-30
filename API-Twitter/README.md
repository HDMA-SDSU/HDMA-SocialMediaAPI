![logo](http://humandynamics.sdsu.edu/images/HDMA_Logo.png)
######*Project conducted by*: San Diego State University
######*Content prepared by*: Jiue-An (Jay) Yang @ San Diego State University

---

## Using the Search API (with Python)

Among many popular social media and social networking services, Twitter is kind enough to provide powerful and relatively friendly API for developers to interact with the Twitter database.  In this tutorial, we will go through the steps of setting up and using the Twitter Search API.  The Twitter API can be accessed with many computer programming language, in this tutorial we use Python to demonstrate how to use the Twitter Search API and access Twitter data (tweets). 

---

#### Prerequisite

##### Python version 2.x or 3.x

Python is a popular computer programming language created by Guido van Rossum.
It's currently ranked # 4 by [the IEEE Spectrum’s 2014 Ranking](http://goo.gl/CSfla6).

To learn more about Python, check out the official website at (https://www.python.org/doc/
Python can be downloaded at https://www.python.org/download
 
##### Twitter API Libraries for Python

There are many existing API libraries (wrappers) for Python and they tend to make it easier to work with the Twitter APIs.
A list of Python wrappers for Twitter APIs can be found at https://dev.twitter.com/docs/twitter-libraries.
Navigate to the Python section and install the one of your own choice.   In this tutorial,  we select the library called *tweepy*.

Instructions of installing *tweepy* and its documentation can be found at https://github.com/tweepy/tweepy

---

#### Getting Started

##### Obtain your API keys.
- Create a Twitter account
- Sign up a Twitter account at https://twitter.com/
- Log on to Twitter Developer (https://dev.twitter.com/) and sign in with the Twitter account you just created. 
- Create your Twitter application and generate your API keys/Tokens.  You can follow the tutorial at: [*How to Register a Twitter App in 8 Easy Steps*](http://iag.me/socialmedia/how-to-create-a-twitter-app-in-8-easy-steps/)

##### Write Python codes with your API keys to search 

Once you have Python and the tweepy library installed, you are ready to search for the tweets.
The following codes demonstrates how to (1) setup the API Keys and (2) perform a search at the Twitter database.

- (1) setup your API keys with tweepy (credit to tweepy for this example at: [**tweepy oauth example**](https://github.com/tweepy/tweepy/blob/master/examples/oauth.py) )
```python
import tweepy  # the Twitter API wrapper
import json    # for processing the JSON return later

# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "OAuth settings")
consumer_key=""
consumer_secret=""

# The access tokens can be found on your applications's Details
# page located at https://dev.twitter.com/apps (under "Your access token")
access_token=""
access_token_secret=""

# authenticate your key with oauth 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.secure = True
auth.set_access_token(access_token, access_token_secret)

# setup the API with your Keys
# also, format the return in JSON
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
```

- (2) Now that your endpoint is authenticated with your API keys, we can test the Search API.  Here we use a search for tweets containing the term **"coffee"** around **5 miles radius** from the center of **San Diego State University campus**.  For displaying, we will only search for *the latest tweet*.

```python
# Note: continue from the previous codes

# Calling the search method, with several parameter 
# q: querying keyword
# geocode: filter the return tweets that are within the spatial restrictions
# count: limits the numbers of return
results = api.search(q="coffee", geocode = "32.774575,-117.072404,5mi", count=1)

# display the search results
print json.dumps(results, indent =4)
```

- (3) Check out the return tweet! As you can see, the return contains many attributes that can be analyzed, such as *text*, *created_at*, and its *location*. (Note: some returned attributes are not displayed to cut down the size of the page)   

```json

{
    "search_metadata": {
        "count": 1, 
        "completed_in": 0.059, 
        "max_id_str": "671242629179314176", 
        "since_id_str": "0", 
        "next_results": "?max_id=671171507318423554&q=coffee&geocode=32.774575%2C-117.072404%2C5mi&count=1&include_entities=1", 
        "refresh_url": "?since_id=671242629179314176&q=coffee&geocode=32.774575%2C-117.072404%2C5mi&include_entities=1", 
        "since_id": 0, 
        "query": "coffee", 
        "max_id": 671242629179314176
    }, 
    "statuses": [
        {
            "contributors": null, 
            "truncated": false, 
            "text": "RT @thefrenchelf: #ArdeeLovesCoffee Holiday on the go. #coffeeaddict #coffee \n\n#thatsdarling #livefolk #lifecaptured\u2026 https://t.co/HccWgy93\u2026", 
            "is_quote_status": false, 
            "in_reply_to_status_id": null, 
            "id": 671242629179314176, 
            "favorite_count": 0, 
            "source": "<a href=\"http://jeremy98790.webs.com\" rel=\"nofollow\">Jeremy987901912</a>", 
            "retweeted": false, 
            "coordinates": null, 
            "entities": {
                "symbols": [], 
                "user_mentions": [
                    {
                        "id": 2971257370, 
                        "indices": [3,16], 
                        "id_str": "2971257370", 
                        "screen_name": "thefrenchelf", 
                        "name": "a r d e e"
                    }
                ], 
                "hashtags": [
                    {
                        "indices": [18,35], 
                        "text": "ArdeeLovesCoffee"
                    }, 
                    {
                        "indices": [55,68], 
                        "text": "coffeeaddict"
                    }, 
                    {
                        "indices": [69,76], 
                        "text": "coffee"
                    }, 
                    {
                        "indices": [79,92],
                        "text": "thatsdarling"
                    }, 
                    {
                        "indices": [93,102],
                        "text": "livefolk"
                    }, 
                    {
                        "indices": [103,116],
                        "text": "lifecaptured"
                    }
                ], 
                "urls": [
                    {
                        "url": "https://t.co/HccWgy93Dn", 
                        "indices": [118,140],
                        "expanded_url": "https://instagram.com/p/-ri7SOzgkl/", 
                        "display_url": "instagram.com/p/-ri7SOzgkl/"
                    }
                ]
            }, 
            "in_reply_to_screen_name": null, 
            "in_reply_to_user_id": null, 
            "retweet_count": 5, 
            "id_str": "671242629179314176", 
            "favorited": false, 
            "user": {
                "follow_request_sent": false, 
                "has_extended_profile": false, 
                "profile_use_background_image": true, 
                "default_profile_image": false, 
                "id": 3682168996, 
                "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme1/bg.png", 
                "verified": false, 
                "profile_text_color": "333333", 
                "profile_image_url_https": "https://pbs.twimg.com/profile_images/644371870356107264/zUtpAElb_normal.jpg", 
                "profile_sidebar_fill_color": "DDEEF6", 
                "entities": {
                    "description": {
                        "urls": []
                    }
                }, 
                "followers_count": 182, 
                "profile_sidebar_border_color": "C0DEED", 
                "id_str": "3682168996", 
                "profile_background_color": "C0DEED", 
                "listed_count": 99, 
                "is_translation_enabled": false, 
                "utc_offset": null, 
                "statuses_count": 1952, 
                "description": "Health Promoter \u272a Triathlete \u272a Dublin born \u272a Mindful", 
                "friends_count": 988, 
                "location": "", 
                "profile_link_color": "0084B4", 
                "profile_image_url": "http://pbs.twimg.com/profile_images/644371870356107264/zUtpAElb_normal.jpg", 
                "following": false, 
                "geo_enabled": false, 
                "profile_background_image_url": "http://abs.twimg.com/images/themes/theme1/bg.png", 
                "screen_name": "Jeremy98790", 
                "lang": "en", 
                "profile_background_tile": false, 
                "favourites_count": 89, 
                "name": "Jeremy Raske", 
                "notifications": false, 
                "url": null, 
                "created_at": "Thu Sep 17 04:46:12 +0000 2015", 
                "contributors_enabled": false, 
                "time_zone": null, 
                "protected": false, 
                "default_profile": true, 
                "is_translator": false
            }, 
            "geo": null, 
            "in_reply_to_user_id_str": null, 
            "possibly_sensitive": false, 
            "lang": "en", 
            "created_at": "Mon Nov 30 08:21:28 +0000 2015", 
            "in_reply_to_status_id_str": null, 
            "place": null, 
            "metadata": {
                "iso_language_code": "en", 
                "result_type": "recent"
            }
        }
    ]
}

```

##### Concluding Notes

For more information about the search parameters that can be used in your query,
visit the official Twitter developer website at https://dev.twitter.com/

Thank you for checking out our page.