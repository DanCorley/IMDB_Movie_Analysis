# create a unique list of the genres
set_of_lists = set([y for x in [a.split(',') for a in imdb_basics['genres']] for y in x])

# iterate through series to show if 'genres' column contains genre
def genre_finder(genre, cell):
    if genre in cell:
        return 1
    return 0

# iterate through set_of_lists and create a new column for each genre
def column_creator(set_of_lists):
    for genre in set_of_lists:
        imdb_basics[genre] = imdb_basics['genres'].map(lambda cell: genre_finder(genre, cell))