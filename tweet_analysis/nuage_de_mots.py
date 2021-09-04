import tweepy as tw
import textblob as tb
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import nltk
from nltk.corpus import stopwords
from tweet_analysis.collect_tweets import collect_tweets_from_listkeywords_to_database
from PIL import Image


def word_used(dataframe_tweets) :
    phrase_tweets_1 = dataframe_tweets.Text #liste contenant les textes des tweets
    phrase_tweets = []
    d_ensemble_tweets = {}
    for tweet_text in phrase_tweets_1 :
        phrase_tweets.append(tb.TextBlob(tweet_text))
    for text in phrase_tweets :
        d_tweet={}
        for word in text.words :
            if word.capitalize() not in d_tweet :
                d_tweet[word.capitalize()] = text.words.count(word)
        for word in d_tweet :
            if word in d_ensemble_tweets :
                d_ensemble_tweets[word]+=d_tweet[word]
            else:
                d_ensemble_tweets[word] = d_tweet[word]
    return d_ensemble_tweets

def display_wordcloud(d_tweet_frequency) :
    mask_image=np.array(Image.open("images/logo_twitter.jpg"))
    Stopwords = set(stopwords.words('french'))
    Stopwords.update(["rt", "Rt", "twitter", "tweet",",",".",":",";",".","'","https","url",'a','the','to', 'in','and', 'for', 'of'])
    d_tweet_frequency_stopwords = {}
    for cle in d_tweet_frequency :
        if cle.lower() not in Stopwords :
            d_tweet_frequency_stopwords[cle] = d_tweet_frequency[cle]
    wordcloud = WordCloud(stopwords=Stopwords, background_color="white", max_words=100, mask=mask_image).fit_words(d_tweet_frequency_stopwords)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.title("Liste des mots les plus utilisés", fontsize = 25)
    plt.axis("off")
    plt.show()


#Test : display_wordcloud(word_used(collect_tweets_from_listkeywords_to_database(['Giletjaune'])))


def hashtags(dataframe_tweets) :
    """
    Prend en paramètre un dataframe pandas de tweet
    et renvoi un dictionnaire contenant les hashtags
    de tous les tweets et le nombre de fois qu'il
    est utilisé dans les tweets.
    """
    dict_hashtags = {}
    for dic in dataframe_tweets['Hashtags'] :
        for cle in dic :
            if cle in dict_hashtags :
                dict_hashtags[cle]+=dic[cle]
            else :
                dict_hashtags[cle] = dic[cle]
    return dict_hashtags


def display_wordcloud_hashtag(d_hashtag_frequency) :
    mask_image=np.array(Image.open("images/logo_twitter.jpg"))
    wordcloud = WordCloud(background_color="white", max_words=100, mask = mask_image).fit_words(d_hashtag_frequency)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.title("Liste des # les plus utilisés", fontsize = 25)
    plt.axis("off")
    plt.show()

#test : display_wordcloud_hashtag(hashtags(collect_tweets_from_listkeywords_to_database(['JO2020'])))