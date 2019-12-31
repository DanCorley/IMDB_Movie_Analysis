
## TN

# convert 'release_date' to datetime
tn['release_date'] = pd.to_datetime(tn['release_date'])

# add month and year calculations
tn['release_year'] = tn['release_date'].dt.year
tn['release_month'] = tn['release_date'].dt.month

# convert all dollar amounts to type integer
tn['production_budget'] = tn['production_budget'].replace('[\$,]','',regex=True)astype('int64')
tn['domestic_gross'] = tn['domestic_gross'].replace('[\$,]','',regex=True).astype('int64')
tn['worldwide_gross'] = tn['worldwide_gross'].replace('[\$,]','',regex=True).astype('int64')




## BOM

# fill N/As in the 'foreign_gross' column
bom.foreign_gross = bom.foreign_gross.fillna(0)




## RT

# read RT data files
rt_movie_info = pd.read_csv('../Expanded CSVs/rt.movie_info.tsv', sep='\t')

# convert to datetime formats
rt_movie_info['theater_date'] = pd.to_datetime(rt_movie_info['theater_date'])
rt_movie_info['dvd_date'] = pd.to_datetime(rt_movie_info['dvd_date'])

# adding month and year to columns
rt_movie_info['release_year'] = rt_movie_info['theater_date'].dt.year
rt_movie_info['release_month'] = rt_movie_info['theater_date'].dt.month

# fill all NA box office values with 0
rt_movie_info['box_office'].fillna(0, inplace=True)

# filter out genres that have less than 5 instances
rt_movie_info[rt_movie_info.groupby('genre')['genre'].transform('count') > 5]

# line plot of the release year and $
sns.lineplot(x="release_year", y="box_office", data=rt, ci=None, hue='genre');


##### create new columns for the genres in the genre columns

set_of_lists = set([y for x in [a.split('|') for a in rt['genre']] for y in x]) 

def genre_finder(genre, cell):  # function show if the genre is within set_of_lists
    if genre in cell:
        return 1
    return 0

def column_creator(set_of_lists):   # create columns for all the set_of_lists and see if the 
    for genre in set_of_lists:
        rt[genre] = rt['genre'].map(lambda cell: genre_finder(genre, cell))
        
#####