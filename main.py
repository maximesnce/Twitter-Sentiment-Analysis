from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from PIL import ImageTk, Image
import random

"""
Ces variables globales permettent de modifier les recherches en fonctions des boutons selectionnes
"""
global user, topic, athlete, keywords
user = "@Olympics"
topic = "JO2020"
athlete = "@johannedefay"
keywords = []

"""
Differentes fonctions qui vont etre appeles par des boutons
"""
def polarity():
    """
    Affiche la polarity des 100 derniers tweets de user
    """
    plot_polarity(collect_by_user(user,100))
    plt.show()

def wordcloud():
    """
    Affiche un wordcloud par rapport au topic
    """
    display_wordcloud_hashtag(hashtags(collect_tweets_from_listkeywords_to_database([topic])))

def popularite():
    """
    Affiche la popularite d'un athlete
    """
    plot_tweets(collect_by_user(athlete, 100))
    plt.show()

def top_twittos():
    """
    Affiche les top twittos pour la recherche avec "keyword"
    """
    if keywords != []:
        data_frame = collect_tweets_from_listkeywords_to_database(keywords)
        nb_followers(data_frame)
        evolution_rt_like(data_frame)
        part1,part2,part3 = blob_sentiment_analysis(data_frame)
        messagebox.showinfo("Resultats", part1 + "\n" + part2 + "\n" + part3)
    else:
        messagebox.showinfo("Erreur", "Aucune selection (donc pas de mots cles a chercher!)")

"""
Création de la fenêtre principale Mafenetre avec tkinter (main window)
"""
Mafenetre = Tk()


"""
Met en place l'image des JO en background
Nomme la fenetre et la dimensionne
"""
background_image = ImageTk.PhotoImage(Image.open("images/JO.jpg"))
background_label = Label(Mafenetre, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


Mafenetre.title('Application JO')
Mafenetre.geometry('1000x800+800+400')

"""
Importe les differentes fonctions qu'on va mettre en oeuvre
"""
from tweet_analysis.graphique import *
from tweet_analysis.nuage_de_mots import *
from tweet_analysis.Useful_data import *
from tweet_analysis.sentiment_analysis import *
from tweet_analysis.nuage_de_mots import *
from tweet_analysis.graphique import *
from tweet_analysis.positivity_by_country import *

#Données remplies au préalables, sélectionnées par nos soins

list_keywords = ['JO2020', 'Tokyo2020', 'Japan2020','Olympics2020','OlympicsGame2020','Sport2020']
list_keywords_english = ['Olympics', 'Olympics AND Mbappé', 'Olympics AND France', 'Olympics AND french']


#Collecte des tweets à partir de la liste de mots clefs et retourne une data frame avec les éléments pertinents
data_frame = collect_tweets_from_listkeywords_to_database(list_keywords)

print(nb_followers(data_frame))
print(evolution_rt_like(data_frame))
print(blob_sentiment_analysis(data_frame))
print(display_wordcloud(word_used(data_frame)))
print(display_wordcloud_hashtag(hashtags(data_frame)))
print(affichage(collect_and_analyse('Olympics2020')))
