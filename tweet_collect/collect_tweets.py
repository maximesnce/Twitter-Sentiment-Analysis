import tweepy
# We import our access keys:
from credentials import *   
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json

def twitter_setup():
    """
    Utility function to setup the Twitter's API
    with an access keys provided in a file credentials.py
    :return: the authentified API
    """
    # Authentication and access using keys:
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    # Return API with authentication:
    api = tweepy.API(auth)
    return api

def collect_by_user(user_id, number = 100):
    """
    Collecte number tweets de user_id
    Retourne les tweets
    """
    connexion = twitter_setup()
    statuses = connexion.user_timeline(id = user_id, count = number)
    return statuses

def collect_by_keywords(keywords,nb,lg="french"):
    connexion = twitter_setup()
    tweets = connexion.search(keywords,language=lg,count=nb)
    return tweets

def get_hashtags(tweet):
    """
    Prend en argument un tweet et retourner une liste de hashtags
    """
    hashtags_liste = []
    hashtags = tweet.entities.get("hashtags")
    for hashtag in hashtags :
        if hashtag['text'] in hashtags_liste:
            pass
        else:
            hashtags_liste.append(hashtag["text"])
    return hashtags_liste

def transformation(tweets):
    """
    Transforme un ensemble de tweets en un tableau panda  --> on extrait l'id, le texte, la date de creation, les hashtags, le nombre de likes et les retweets
    """
    tableau = [[] for i in range(len(tweets))]
    for i,tweet in enumerate(tweets):
        tableau[i].append(tweet.id)
        tableau[i].append(tweet.user.screen_name)
        tableau[i].append(tweet.text)
        tableau[i].append(tweet.created_at)
        tableau[i].append(get_hashtags(tweet))
        tableau[i].append(tweet.user.location)
        tableau[i].append(tweet.favorite_count)
        tableau[i].append(tweet.retweet_count)
        tableau[i].append(tweet.user.followers_count)
    return pd.DataFrame(tableau,["Tweet "+str(i+1) for i in range(len(tweets))],columns = ["id","Nom","Text","Date","Hashtag","Location","Like","Retweets","Followers"])

print(transformation(collect_by_keywords("2020",100)))


#Autre fonction de collect qui permet de partir d'une liste de mots cléfs pour aboutir à une dataframe

def get_tweets_from_candidates_search_queries(queries,twitter_api=twitter_setup()):
    d={}
    for query in queries :
        d[query] = twitter_api.search(query,language=["french"],rpp=2, count = 100)
    return d

def from_dictionnary_to_database(dictionnary,list_key_words):
    data_frame = pd.DataFrame(columns=['User_name', 'Nb_followers', 'Text', 'Hashtags', 'RT', 'Like', 'Location', 'Date'])
    for keyword in list_key_words :
        for tweet in dictionnary[keyword] :
            data_frame = data_frame.append({'User_name': tweet.user.screen_name, 'Nb_followers': tweet.user.followers_count, 'Text': tweet.text, 'Hashtags': get_hashtags(tweet), 'RT': tweet.retweet_count, 'Like': tweet.favorite_count, 'Location': tweet.user.location, 'Date': tweet.created_at}, ignore_index=True)
    return data_frame


def collect_tweets_from_listkeywords_to_database(list_keywords):
    d = get_tweets_from_candidates_search_queries(list_keywords)
    data_frame = from_dictionnary_to_database(d, list_keywords)
    return data_frame

def store_tweets(tweets,filename):
    """Cree un fichier json dans filename qui stocke les tweets donne en entree"""
    list_tweets = []
    for tweet in tweets :
        tweet_infos = {}
        tweet_infos["tweet_id"] = tweet.id
        tweet_infos["user_name"] = tweet.user.screen_name
        tweet_infos["tweet_text"] = tweet.text
        tweet_infos["tweet_date"] = str(tweet.created_at)
        tweet_infos["hashtags"] = get_hashtags(tweet)
        tweet_infos["location"] = tweet.user.location
        tweet_infos["favorite_count"] = tweet.favorite_count
        tweet_infos["retweet_count"] = tweet.retweet_count
        tweet_infos["followers_count"] = tweet.user.followers_count
        list_tweets.append(tweet_infos)
    with open( filename + ".json" , "w+" ) as write_filename :
        json.dump(list_tweets, write_filename, indent=4) # indent=4 permet d'eclater l'affichage du json

def traduit(path):
    with open(path, 'r') as f:
        donnees = json.load(f)
    return donnees

def collect_replies(tweet_id,user_name):
    reponses_possible=collect("to:"+user_name,language=None)
    replies=[]
    for reponse in reponses_possibles:
        if reponse.in_reply_to_status_id == tweet_id:
            replies.append(reponse)
    return replies


