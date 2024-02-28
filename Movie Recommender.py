#Please copy the completed functions from the two code windows above into this active code window. Next, you’ll write a function, called get_related_titles. It takes a list of movie titles as input. It gets five related movies for each from TasteDive, extracts the titles for all of them, and combines them all into a single list. Don’t include the same movie twice.

import json
import requests_with_caching

def get_movies_from_tastedive(tags_string):
    baseurl = "https://tastedive.com/api/similar"
    movie_diction = {}
    movie_diction["q"] = tags_string
    movie_diction["type"] = "movies"
    movie_diction["limit"] = 5
    movies_resp = requests_with_caching.get(baseurl, params = movie_diction)
    return movies_resp.json()

def extract_movie_titles(movie):
    return [d["Name"]for d in movie["Similar"]["Results"]]

def get_related_titles(related):
    lst_of_related_movies = []
    for var in related:
        movies = extract_movie_titles(get_movies_from_tastedive(var))
        for movie in movies:
            if movie not in lst_of_related_movies:
                lst_of_related_movies.append(movie)        
    return lst_of_related_movies
