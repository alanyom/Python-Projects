#Define a function, called get_movies_from_tastedive. It should take one input parameter, a string that is the name of a movie or music artist. The function should return the 5 TasteDive results that are associated with that string; be sure to only get movies, not other kinds of media. It will be a python dictionary with just one key, ‘Similar’.

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

d = get_movies_from_tastedive("Black Panther")
print(d)
