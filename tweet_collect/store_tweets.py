from collect_tweets import *
import json


def store_tweets(tweets,file):
    """cette fonction suavegarde les données importantes des tweets dans le dossier file (chaine de caractères)"""
    
    with open(file,"w") as tweets_file:
        for tweet in tweets:
            #on sauvegarde les informations importantes dans un dictionnaire pour chaque tweet
            tweet_to_save={}
            tweet_to_save['tweet_id']=tweet.id
            tweet_to_save['user']=tweet.user.screen_name
            tweet_to_save['text']=tweet.text
            tweet_to_save['date']=str(tweet.created_at)
            tweet_to_save['hashtags']=(tweet.entities)['hashtags']
            tweet_to_save['location']=tweet.user.location
            tweet_to_save['retweets']=tweet.retweet_count
            tweet_to_save['likes']=tweet.favorite_count
            tweet_to_save['abonnés']=tweet.user.followers_count
            tweet_to_save["language"]=tweet.lang
            #put infos in a tuple
            json.dump(tweet_to_save,tweets_file)
            #on saut une kigne après chaque tweet
            tweets_file.write("\n")

tweets=collect_by_keywords("Emmanuel Macron",10,lg="french")
store_tweets(tweets,"data.json")




        
