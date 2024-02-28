#Please copy the completed function from above into this active code window. Now write a function called get_movie_rating. It takes an OMDB dictionary result for one movie and extracts the Rotten Tomatoes rating as an integer. For example, if given the OMDB dictionary for “Black Panther”, it would return 97. If there is no Rotten Tomatoes rating, return 0.

import requests_with_caching
import json

def get_movie_data(data):
    url = "http://www.omdbapi.com/"
    param_diction = {}
    param_diction["t"] = data
    param_diction["r"] = "json"
    resp = requests_with_caching.get(url, params = param_diction)
    return resp.json()

def get_movie_rating(inputt):
    for x in inputt["Ratings"]:
        if x["Source"] == "Rotten Tomatoes":
            return int(x['Value'][:-1])
    return 0
            
            
            
print(get_movie_rating(get_movie_data("Deadpool 2")))
