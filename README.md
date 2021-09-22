# Twitter-Sentiment-Analysis
Use of the Twitter API to retrieve and analyze data regarding the Olympics

# Groupe numéro: 4
Benjamin Boucher  
Louis Delort  
Antoine Desgranges  
Victor Petitdemange  
Maxime Seince

__Projet sur la collecte et l'analyse de tweets en rapport avec les Jeux-Olympiques__  

*Imports: tweepy, geotext, geocoder (+ API), pyplot, pandas, textblob, tkinter, random, wordcloud, ntlk, pillow, json, folium*  

# I. twitter_connection_setup  
Ce dossier contient uniquement le module API_connection qui permet de se connecter à l'API twitter avec les clés du compte developer. Cela est utile pour les fonctions de collecte du module collect_tweets.  

# II. tweet_collect  

Dans ce dossier, on ne fait pas de différence entre les objets tweet et status. 

## 1. collect_tweets  
* Il s'agit du module comportant l'ensemble des fonctions permettant la collecte de tweets.  
* On peut collecter les tweets d'un utilisateur donné, ou faire une recherche de tweets par mots clés.  
* La fonction get_hashtags permet d'obtenir la liste des hashtags présents dans un tweet donné. Cette fonction renvoie une liste. Elle sert notamment à créer le word cloud des hashtags les plus utilisés. (cf. II.2)  
* A partir de tweets, la fonction from_statuses_to_dataframe renvoie un tableau panda contenant les informations importantes des tweets dont on peut avoir besoin dans d'autres fonctions (ID, texte, likes, retweets...).  
* La fonction collect_by_search_queries permet de collecter des tweets à partir de requêtes. 
* Les fonctions from_dictionnary_to_dataframe et collect_tweets_from_listkeywords_to_dataframe permettent de convertir ces objets en dataframe.   
* La fonction collect_replies permet de récupérer les réponses à un tweet d'un utilisateur.

## 2. store_tweets
* La fonction store_tweets permet le stockage de tweets dans un fichier json.  
* La fonction read_tweets permet de récupérer les données contenues dans un fichier .json  

## 3. fill_json  
La fonction stock_tweets a été créée pour pouvoir collecter plus de 100 tweets : on appelle collect_by_keywords (située dans collect_tweets) et store_tweets et on collecte des tweets pour une liste de mots clés et non plus un seul mot clé (on collecte 100 tweets par requête).  

## 4. location  
Ce module a pour objectif de créer une carte avec les positions des personnes ayant tweeté à propos d'un mot clé (Olympics par exemple). On y trouve les fonctions suivantes : 
* location : utilise geotext pour extraire les villes et pays où les tweets ont été rédigés  
* locations : renvoie un dictionnaire avec toutes ces villes et pays et le nombre d'occurences de chacun  
* lat-long : utilise geocoder pour trouver les latitudes et longitudes  
* create-map : permet la création d'une carte montrant chacun de ces localisations avec le module folium  

 

# III. data

Il s'agit d'une base de données dans laquelle sont stockés de nombreux tweets. Elle sera utilisée dans les modules qui suivent.  

# IV. tweet_analysis

## 1. graphique  
Le but des fonctions présentes dans ce module est d'extraire d'un ensemble de tweets, celui qui a le plus de retweets, le plus de likes ou qui est le plus polarisé, ou d'extraire l'utilisateur qui a le plus de followers. 

## 2. nuage_de_mots  
Ce module permet de créer un wordcloud avec les mots ou les hashtags les plus fréquemment utilisés sur twitter en rapport avec un thème donné.

## 3. positivity_by_country
La première fonction de ce module permet de déterminer la localisation de l'auteur d'un tweet. Puis on détermine la polarité des tweets par zones géographiques et enfin on affiche le résultat sous forme d'histogramme. 

## 4. sentiment_analysis  
Ce fichier contient une fonction qui renvoie un dictionnaire comportant le nombre de tweets positifs, neutres et négatifs. Pour le créer, on récupère les textes de tweets et on analyse leur polarité grâce à une fonctionnalité du module textblob. On retourne enfin un graphique contenant les proportions de tweets positifs, neutres et négatifs.  

## 5. sports_et_athletes  
Ce fichier contient deux fonctions qui permettent, à partir d'une liste d'athlètes ou de sports, de déterminer ceux dont on parle le plus sur twitter. Elles renvoient toutes les deux une liste contenant les sports ou athlètes par ordre décroissant d'importance d'apparition dans les tweets à propos des JO de 2020.  

## 6. useful_data  
Dans ce module, on trouve des fonctions variées qui peuvent être utiles au reste de l'étude. A partir d'un dataframe, la fonction most_famous_account renvoie le tweet avec le plus de retweets et ce nombre, et l'utilisateur le plus suivi et le nombre de followers. La fonction nb_followers renvoie le classement des 10 utilisateurs tweetant à propos d'un thème donné les plus suivis. Enfin, la fonction evolution_rt_like renvoie un graphique montrant l'évolution des retweets et likes de tweets obtenus dans un dataframe panda.  

# V. images
Regroupe les images utilisées par les fonctions des autres modules (logo JO et logo Twitter)

# VI. main  
Il s'agit du fichier à exécuter pour obtenir toutes les informations utiles d'un seul coup. Cela se traduit par une interface graphique qui permet d'afficher à peu près tout type de données en lien avec les Jeux Olympiques de 2020. 
