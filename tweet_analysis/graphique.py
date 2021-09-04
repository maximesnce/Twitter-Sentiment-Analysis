from tweet_analysis.collect_tweets import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from textblob import TextBlob

def plot_tweets(tweets, details =""):
    """
    plot les likes et les retweets de tweets (n'affiche rien)
    details est un string (par defaut vide) qui ajoute des informations sur ce qui est plot
    """
    data = transformation(tweets)
    tfav = pd.Series(data=data['Like'].values, index=data['Date'])
    tret = pd.Series(data=data['Retweets'].values, index=data['Date'])
    # Likes vs retweets visualization:
    tfav.plot(figsize=(16,4), label="Likes " + details, legend=True)
    tret.plot(figsize=(16,4), label="Retweets " + details, legend=True)

def plot_polarity(tweets, details = ""):
    """
    plot la polarity de tweets (ne l'affiche pas)
    details est un string (par defaut vide) qui ajoute des informations sur ce qui est plot
    """
    data = transformation(tweets)
    polarity = []
    for tweet_text in data["Text"]:
        polarity.append(TextBlob(tweet_text).sentiment.polarity)
    tfav = pd.Series(data=polarity, index=data['Date'])
    # Likes vs retweets visualization:
    tfav.plot(figsize=(16,4), label="polarity " + details, legend=True)

def max_retweet(tweets):
    """
    Extrait le tweet avec le plus de retweet d'un ensemble de tweet
    """
    data = transformation(tweets).to_numpy()
    max = 0
    best_tweet = data[0][2]
    for tweet in data:
        if tweet[-1] > max:
            max = tweet[-1]
            best_tweet = tweet[2]
    return best_tweet

def max_like(tweets):
    """Extrait le tweet avec le plus de like d'un ensemle de tweet"""
    data = transformation(tweets).to_numpy()
    max = 0
    best_tweet = data[0][2]
    for tweet in data:
        if tweet[-2] > max:
            max = tweet[-2]
            best_tweet = tweet[2]
    return best_tweet


def max_followers(tweets):
    """Extrait le tweet de l'utilisateur ayant le plus de followers"""
    max=0
    best_tweet=tweets[0]
    for k in range(len(tweets)):
        tweet=tweets[k]
        if tweet.user.followers_count > best_tweet.user.followers_count:
            best_tweet=tweet
    return best_tweet


def max_polarity (tweets):
    """Extrait le tweet avec le plus de polarity d'un ensemle de tweet"""
    max = 0
    data = transformation(tweets).to_numpy()
    best_tweet = data[0][2]
    for tweet in data:
        if TextBlob(tweet[2]).sentiment.polarity > max:
            max = TextBlob(tweet[1]).sentiment.polarity
            best_tweet = tweet[2]
    return best_tweet


#plot_polarity(collect_by_user("@SpecialOlympics"), "@SpecialOlympics")
##plot_polarity(collect_by_user("@Olympics"), "@SpecialOlympics")
#plot_polarity(collect_by_user("@NBCOlympics"), "@NBCOlympics")

#plt.show()

#tweets=collect_by_keywords("Emmanuel Macron",15,lg="french")
#tweet=max_followers(tweets)
#print(tweet.text,tweet.user.followers_count)
