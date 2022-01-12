# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 13:40:24 2022

@author: Umut Hasret
"""

import pandas as pd
import re
import string
import ast


def preProcessData(df):
    for index, row in df.iterrows():
        # get full_text of the tweet
        if row['truncated']:
            tweet = {"full_text": ast.literal_eval(row['extended_tweet'])['full_text']}
        else:
            # if the tweet is retweeted, this status will not be na
            if ('retweeted_status' in row) and (not pd.isna(row['retweeted_status'])):
                originalTweet = ast.literal_eval(row['retweeted_status'])
                userTagName = originalTweet['user']['screen_name']

                # if the text is truncated
                if originalTweet['truncated']:
                    tweet = {"full_text": "RT @" + userTagName + ": " + originalTweet['extended_tweet']['full_text']}
                else:
                    tweet = {"full_text": "RT @" + userTagName + ": " + originalTweet['text']}

                del originalTweet
                del userTagName

            # if the tweet is original and not truncated
            else:
                tweet = {"full_text": row['text']}

        # get Username & User Tag & Location & Verification status of account
        tweet["username"] = ast.literal_eval(row['user'])['name']
        tweet["screen_name"] = ast.literal_eval(row['user'])['screen_name']
        tweet["location"] = ast.literal_eval(row['user'])['location']
        tweet["is_verified"] = ast.literal_eval(row['user'])['verified']

        # get Quote & Fav & RT & Reply counts
        tweet["quote_count"] = row['quote_count']
        tweet["favorite_count"] = row['quote_count']
        tweet["retweet_count"] = row['retweet_count']
        tweet["reply_count"] = row['reply_count']

        # get Tweet creation date&time
        tweet["created_at"] = row['created_at']

        # get TweetID
        tweet["tweet_id"] = row['id']

        # add to the list
        if not pd.isna(tweet['location']):
            tweets.append(tweet)

        del tweet
        del row
        del index


def countNumberOfRetweetedTweets(tweets):
    # Separate RTs and original tweets
    for tweet in tweets:
        if bool(re.match(r'(RT @[\w]+:)', tweet["full_text"])):
            rts.append(tweet)
        else:
            non_rt.append(tweet)
        del tweet


def countTweetsFromVerifiedAccounts(tweets):
    # Distinguish tweets according to their account verification status    
    for tweet in tweets:
        if tweet["is_verified"]:
            tweets_from_verified_accounts.append(tweet)
        else:
            tweets_from_regular_accounts.append(tweet)

        del tweet


# filter locations according to city names given in listOfCities
def filterLocations(tweets, listOfCities):
    filtered_tweets = []

    for tweet in tweets:
        for index, city in listOfCities.iterrows():
            if city['city'] in tweet['location']:
                filtered_tweets.append(tweet)
                break
    return filtered_tweets


# Main

df = pd.read_csv('../raw_data/justicefornaseembibi.csv')
df1 = pd.read_csv('../raw_data/justiceforgulpanra.csv')
df2 = pd.read_csv('../raw_data/justiceforsaima.csv')
df3 = pd.read_csv('../raw_data/justicefornoor.csv')
df4 = pd.read_csv('../raw_data/savewomenofpakistan.csv')

pakistanCities = pd.read_csv('../pakistanCities.csv')
egyptCities = pd.read_csv('../egyptCities.csv')

dfs = [df, df1, df2, df3, df4]

tweets = []
tweets_from_verified_accounts = []
tweets_from_regular_accounts = []

rts = []
non_rt = []

# preprocess all the given hashtags and build 
for df_instance in dfs:
    preProcessData(df_instance)

    del df_instance

countNumberOfRetweetedTweets(tweets)
countTweetsFromVerifiedAccounts(tweets)

original_tweets_from_pakistan = filterLocations(non_rt, pakistanCities)
all_tweets_from_pakistan = filterLocations(tweets, pakistanCities)
