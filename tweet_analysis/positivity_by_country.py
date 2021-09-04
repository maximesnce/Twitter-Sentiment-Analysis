from tweet_analysis.collect_tweets import *
from textblob import TextBlob
import matplotlib.pyplot as plt
from geotext import GeoText

def location(tweet):
    location = tweet.user.location
    place = GeoText(location)
    city = place.cities
    country = place.countries
    return country

def collect_and_analyse(keyword):
    """
    Retourne un dictionnaire de moyenne de polarity par pays des tweets recoltes (format {pays:moyenne_polarity})
    """
    tweets = collect_by_keywords(keyword,100)
    print(len(tweets))
    somme_polarity_par_pays = {}
    # somme_polarity_par_pays contient un dictionnaire {pays:somme_polarity}
    nb_tweet_par_pays = {}
    # nb_tweet_par_pays contient un dictionnaire {pays:nombre_de_tweets_trouve_dans_ce_pays}
    for tweet in tweets:
        if location(tweet) == []: # Si un PAYS n'est pas specifiquement mentionne, on l'ignore
            pass
        elif location(tweet)[0] in somme_polarity_par_pays.keys():
            somme_polarity_par_pays[location(tweet)[0]] += TextBlob(tweet.text).sentiment.polarity
            nb_tweet_par_pays[location(tweet)[0]] += 1
        else:
            somme_polarity_par_pays[location(tweet)[0]] = TextBlob(tweet.text).sentiment.polarity
            nb_tweet_par_pays[location(tweet)[0]] = 1
    moyenne_polarity_par_pays = {}
    for country in somme_polarity_par_pays:
        moyenne_polarity_par_pays[country] = somme_polarity_par_pays[country] / nb_tweet_par_pays[country]
    return moyenne_polarity_par_pays

# print(collect_and_analyse("Paralympics"))

def affichage(moyenne_polarity):
    for country in moyenne_polarity:
        plt.bar(country,moyenne_polarity[country])
    plt.show()

affichage(collect_and_analyse("Olympics"))