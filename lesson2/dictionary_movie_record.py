movie = {}
movie['title'] = "The Godfather"
movie['director'] = "Francis Ford Coppola"
movie['year'] = 1972
movie['rating'] = 9.2


print(movie['year'])
movie["rating"] = (movie["rating"] + 9.3) / 2
print(movie["rating"])


movie['actors'] = ['Marlon Brandon', 'Al Pacino', 'James Caan']
movie['other_details'] = {
    'runtime': 175,
    'language': 'English'
}

print(movie)