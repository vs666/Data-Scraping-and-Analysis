import tweepy
import pandas as pd
import csv
import sys
import re
import string
import preprocessor as p

DELHI_WOE_ID = 20070458
consumer_key = "vcrcz36Okb0ORNmPioVc7BsSr"
consumer_secret = "pO3bjApqstGzNUKXrmRnFwGump4V2BjhNsNBZyywX7MfBnbDCl"
access_key = "740572559175913472-FszGsGTpS1CqhAqtbPgCGmzAx17ElVE"
access_secret = "VTeZM5wv1gK5vCDcnzkAnZApLkO5N7VMV4c5KjaJpJmbe"


fileName = sys.argv[1]
fn1 = open(fileName, 'r')


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)
# del_trends = api.trends_place(DELHI_WOE_ID)
fn = input('Enter csv file name to store scraped data : ')
csvFile = open(fn, 'a')
csvWriter = csv.writer(csvFile)
# new_search = search_words
# trends = fn.readlines()
L = fn1.readlines()
csvWriter.writerow(["timestamp", "text", "username", "location",
                    "following", "followers", "about", "lang", "likes", "retweets"])
for new_search in L:
    print("Searching ", new_search.split('\n')[0])
    for tweet in tweepy.Cursor(api.search, q=new_search.split('\n')[0], count=1000,
                               since_id=0, id=DELHI_WOE_ID).items():
        print(tweet)
        csvWriter.writerow([tweet.created_at, tweet.text.encode(
            'utf-8'), tweet.user.screen_name.encode('utf-8'), tweet.user.location.encode('utf-8'), tweet.user.friends_count, tweet.user.followers_count, tweet.user.description.encode('utf-8'), tweet.lang, tweet.favorite_count, tweet.retweet_count])

