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

(1) setup your API keys with tweepy (credit to tweepy for this example (https://github.com/tweepy/tweepy/blob/master/examples/oauth.py) )

```python
import tweepy

consumer_key=""
consumer_secret=""

access_token=""
access_token_secret=""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.secure = True
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
```