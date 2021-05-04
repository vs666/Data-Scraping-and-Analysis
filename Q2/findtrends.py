import sys
import tweepy
import json
import csv
from datetime import datetime

consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)
 

DELHI_WOE_ID = 20070458
# for i in api.trends_available():
#     if i['name']=='Delhi' or i['name']=='New Delhi':
#         print(i)

delhi_trends = api.trends_place(DELHI_WOE_ID)
trends = json.loads(json.dumps(delhi_trends, indent=1))

filename = "trends_"+ datetime.today().strftime('%Y_%m_%d_%H_%M_%S')+'.txt'
f = open(filename, 'w')
for trend in trends[0]["trends"]:
    f.write(str(trend["name"])+"\n")
f.close()


# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_key, access_secret)

# api = tweepy.API(auth, wait_on_rate_limit=True)
# fn= input('Enter csv file name to store scraped data : ')
# csvFile = open(fn, 'a')
# csvWriter = csv.writer(csvFile)
# search_words = input('Enter search words :')      # enter your words
# new_search = search_words + " -filter:retweets"

# for tweet in tweepy.Cursor(api.search, q=new_search, count=10,
#                            lang="en",
#                            since_id=0).items():
#     csvWriter.writerow([tweet.created_at, tweet.text.encode(
#         'utf-8'), tweet.user.screen_name.encode('utf-8'), tweet.user.location.encode('utf-8')])
