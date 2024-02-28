#Now, you’ll put it all together. Don’t forget to copy all of the functions that you have previously defined into this code window. Define a function get_sorted_recommendations. It takes a list of movie titles as an input. It returns a sorted list of related movie titles as output, up to five related movies for each input movie title. The movies should be sorted in descending order by their Rotten Tomatoes rating, as returned by the get_movie_rating function. Break ties in reverse alphabetic order, so that ‘Yahşi Batı’ comes before ‘Eyyvah Eyvah’.

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

def get_sorted_recommendations(input_movie):
    related = get_related_titles(input_movie)
    recommended_movie = []
    lst_recommended_movie = []
    for y in related:
        e = get_movie_rating(get_movie_data(y))
        recommended_movie.append(e)
    j = list(zip(recommended_movie, related))
    p = sorted(j,key=lambda x:(x), reverse = True)
    for z in p:
        lst_recommended_movie.append(z[1])
    return lst_recommended_movie


print(get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"]))
