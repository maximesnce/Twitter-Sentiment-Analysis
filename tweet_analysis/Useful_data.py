import tweepy as tw
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from credentials import *
from tweet_analysis.collect_tweets import collect_tweets_from_listkeywords_to_database



def most_famous_account(dataframe):
    rt_max  = np.max(dataframe['RT'])
    rt  = dataframe[dataframe.RT == rt_max].index[0]
    print("The tweet with more retweets is: \n{}".format(dataframe['Text'][rt]))
    print("Number of retweets: {}".format(rt_max))
    nb_followers_max = np.max(dataframe['Nb_followers'])
    nb_followers = dataframe[dataframe.Nb_followers == nb_followers_max].index[0]
    print("The tweetos with more followers is: {}".format(dataframe['User_name'][nb_followers]))
    print("Number of followers: {}".format(nb_followers_max))

#test : most_famous_twittos(collect_tweets_from_listkeywords_to_database(['SpecialOlympics']))

def nb_followers(dataframe):
    data_frame = dataframe.sort_values(by='Nb_followers', ascending = False)
    data_frame = data_frame.drop_duplicates(subset = 'Nb_followers')
    twittos = np.array(data_frame['User_name'])[0:10]
    nb_follow_twittos = np.array(data_frame['Nb_followers'])[0:10]
    pos = np.arange(len(twittos))
    bar_width = 0.3
    plt.bar(pos,nb_follow_twittos,bar_width)
    plt.xticks(pos, twittos)
    plt.xlabel('Name', fontsize = 15)
    plt.ylabel('Nb followers', fontsize = 15)
    plt.title('10 Famous Twittos', fontsize = 18)
    plt.show()

#test : nb_followers(collect_tweets_from_listkeywords_to_database(['SpecialOlympics']))

def evolution_rt_like(dataframe_tweets) :
    """
    Prend en paramètre un dataframe pandas de tweet
    et affiche l'évolution de RTs et Likes.
    """
    tfav = pd.Series(data=dataframe_tweets['Like'].values, index=dataframe_tweets['Date'])
    tret = pd.Series(data=dataframe_tweets['RT'].values, index=dataframe_tweets['Date'])

    # Likes vs retweets visualization:
    tfav.plot(figsize=(16,4), label="Likes", legend=True)
    tret.plot(figsize=(16,4), label="Retweets", legend=True)
    plt.xlabel('Date', fontsize = 15)
    plt.ylabel('Nb RTs/Likes', fontsize = 15)
    plt.title('Like VS RTs', fontsize = 18)
    plt.show()

#evolution_rt_like(collect_tweets_from_listkeywords_to_database(['Olympic']))