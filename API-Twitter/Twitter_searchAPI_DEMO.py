'''
Credit to the official tweepy example 
'''

import tweepy, json
# == OAuth Authentication ==

# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "OAuth settings")
consumer_key="your consumer_key"
consumer_secret="your consumer_secret"

# The access tokens can be found on your applications's Details
# page located at https://dev.twitter.com/apps (under "Your access token")
access_token="your access_token"
access_token_secret="your access_token_secret"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.secure = True
auth.set_access_token(access_token, access_token_secret)

# Authenticate 
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

# Call the search function with selected parameters
results = api.search(q="coffee", geocode = "32.774575,-117.072404,5mi", count=2)

# display the returned results, using json.dumps for prettier display
print json.dumps(results, indent =4)