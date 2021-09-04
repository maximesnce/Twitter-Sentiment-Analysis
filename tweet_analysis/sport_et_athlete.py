from tweepy import *
from collect_tweets import *

def sport_we_talk_about_the_most(sports):
#sport dont on parle le plus apparaît en premier
    max = 0
    most_popular = []
    tweets = collect_by_keywords("jo2020", 100, lg="french")
    for sport in sports:
        n=0
        for tweet in tweets:
            tweet_text = tweet.text
            if sport in tweet_text:
                n+=1
        if n > max :
            max = n 
            most_popular = [sport] + most_popular
        elif n <= max :
            most_popular = most_popular + [sport]
    return(most_popular)


def athletes_we_talk_about_the_most(athletes):
#l'athlète dont on parle le plus apparaît en premier
    max = 0
    most_popular = []
    tweets = collect_by_keywords("jo2020", 100, lg="french")
    for athlete in athletes:
        n=0
        for tweet in tweets:
            tweet_text = tweet.text
            if athlete in tweet_text:
                n+=1
        if n > max :
            max = n 
            most_popular = [athlete] + most_popular
        elif n <= max :
            most_popular = most_popular + [athlete]
    return(most_popular)