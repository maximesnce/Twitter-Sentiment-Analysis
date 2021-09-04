import collect_tweets
from collect_tweets import *
from geotext import GeoText
import pandas as pd

#data=transformation(collect_by_keywords("2020",100))['Location']
#print(data[:,])

def location(tweet):
    location=tweet.user.location
    place=GeoText(location)
    city=place.cities
    country=place.countries
    return country,city

def locations(tweets):
    """cette fonction renvoie un dictionnaire contenant les localisations de chacun des tweets"""
    cities_dict={}
    countries_dict={}
    for tweet in tweets:
        countries,cities=location(tweet)
        for cit in cities:
            if cit not in cities_dict:
                cities_dict[cit]=1
            else:
                cities_dict[cit]=cities_dict[cit]+1
        for count in countries:
            if count not in countries_dict:
                countries_dict[count]=1
            else:
                countries_dict[count]=countries_dict[count]+1
    return countries_dict,cities_dict
        














        

