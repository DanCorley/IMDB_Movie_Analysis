Merging

#libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline

#read csv
imdb_basics = pd.read_csv('../Expanded CSVs/imdb.title.basics.csv')
imdb_ratings = pd.read_csv('../Expanded CSVs/imdb.title.ratings.csv')
tn = pd.read_csv('../Expanded CSVs/tn.movie_budgets.csv')
bom = pd.read_csv('../Expanded CSVs/bom.movie_gross.csv')

#merge dataframes
imdb_title_ratings = pd.merge(imdb_basics,imdb_ratings,on="tconst")
imdb_tn = pd.merge(imdb_title_ratings, tn, left_on='primary_title', right_on='movie')
imdb_bom = pd.merge(imdb_title_ratings, bom, left_on='primary_title', right_on='title')

#clean dataframes
imdb_tn.sort_values(by='numvotes', axis=0, ascending=False, inplace=True)
imdb_tn.drop_duplicates(subset='primary_title', keep='first', inplace=True)
imdb_bom.sort_values(by='numvotes', axis=0, ascending=False, inplace=True)
imdb_bom.drop_duplicates(subset='primary_title', keep='first', inplace=True)

#final merge
imdb_tn_bom = pd.merge(imdb_tn, imdb_bom, left_on='primary_title', right_on='primary_title')

