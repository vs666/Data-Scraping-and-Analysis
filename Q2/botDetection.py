import pandas as pd
import csv
import matplotlib.pyplot as plt
import numpy as np
import tweepy
import sys
import re
import string
import preprocessor as p
import math

DELHI_WOE_ID = 20070458
consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""

W_FC = 0.30

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)


def detectBots(screen_name):
    probBot = 0
    user = api.get_user(screen_name)

    '''
        probBot += w_fc * (100/log(Follower_count,4)) /// w_fc is weight of follwer_count  [30 %]
        
        FOR likes, we can use ( number of likes + number of retweets ) / number of tweets as a potential sign for a bot
        [10]*(number of likes + number of retweets + 1)/(number of tweets + 1)   Special case for no retweets
        
        Language independence implies more bot-like nature [multi-lingual tweets more equi-distributed]


    
        humans have non-zero length of description  [done]
        humans usually have urls in description     [done]


        [Advanced]
        lists/ moments etc. absent is a slight indicator of bots (less weighted)    
        skewed distributed tweet on timeline is a significant indicator of bots
        check time-zone of tweeting anything. If randomly distributed than high prob of it being a bot.
    
    '''
    probBot += W_FC*(100/math.log(user.followers_count, 10))
    probBot += 10*(user.favourites_count/user.statuses_count)
    
    if len(str(user.description)) == 0:
        probBot += 10
    # if len(user.url) == 0:
    #     probBot += 3
    
    return probBot

while True:
    usern = input('Enter username : ')
    print(detectBots(usern))
