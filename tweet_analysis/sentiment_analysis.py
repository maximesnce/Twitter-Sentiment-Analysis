import tweepy as tw
import textblob as tb
import pandas as pd
from tweet_analysis.collect_tweets import collect_tweets_from_listkeywords_to_database
from credentials import *
import matplotlib.pyplot as plt

def blob_sentiment_analysis(dataframe_tweets) :
    phrase_tweets_1 = dataframe_tweets.Text #liste contenant les textes des tweets
    phrase_tweets = []
    dict_nb_polarity = {"positive" : 0, "neutral" : 0, "negative" : 0} #dictionnaire contant le nombre de tweet positifs et négatifs
    for tweet_text in phrase_tweets_1 :
        phrase_tweets.append(tb.TextBlob(tweet_text))
    for text_blob in phrase_tweets :
        polarity = text_blob.sentiment.polarity
        if polarity > 0:
            dict_nb_polarity["positive"]+=1
        elif polarity ==0 :
            dict_nb_polarity["neutral"]+=1
        else:
            dict_nb_polarity["negative"]+=1
    n = len(phrase_tweets)
    labels = 'Positive', 'Neutral', 'Negative'
    sizes = [dict_nb_polarity["positive"]/n, dict_nb_polarity["neutral"]/n, dict_nb_polarity["negative"]/n]
    colors = ['green', 'yellow', 'red']
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=0)
    plt.axis('equal')
    plt.title('Pourcentage de Tweets Positifs/Neutres/Négatifs')
    plt.legend()
    plt.show()
    print("Percentage of positive tweets: {} %".format(dict_nb_polarity["positive"]*100/n))
    print("Percentage of neutral tweets: {} %".format(dict_nb_polarity["neutral"]*100/n))
    print("Percentage of negative tweets: {} %".format(dict_nb_polarity["negative"]*100/n))

#test : dataframe = collect_tweets_from_listkeywords_to_database(['Macron'])
#test : blob_sentiment_analysis(dataframe)





