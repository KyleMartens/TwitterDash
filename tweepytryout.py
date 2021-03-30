import tweepy
import t
import json

auth = tweepy.OAuthHandler(t.CONSUMER_KEY, t.CONSUMER_SECRET)
auth.set_access_token(t.ACCESS_TOKEN_KEY, t.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
dogtweets = api.search(q='%23Dog', count = 100)
for x in range(100):
    print(dogtweets['statuses'][x]['place'])
#for x in dogtweets['statuses']:

#    print(x['text'])
#print(dogtweets['statuses'][0]['entities']['hashtags'])
#print(api.rate_limit_status()['resources']['search'])
