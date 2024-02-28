#Please copy the completed function from above into this active code window. Next, you will need to write a function that extracts just the list of movie titles from a dictionary returned by get_movies_from_tastedive. Call it extract_movie_titles.

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

d = extract_movie_titles(get_movies_from_tastedive("Black Panther"))
print(d)
