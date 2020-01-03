# Movie Data Analysis
### By: Dan Corley & Jeff Lindberg

## Executive Summary
The goal of this analysis is to explore what type of films are currently doing the best at the box office. We analyzed datasets from IMDB and The Numbers to determine which genre had the highest profits. We also wanted to see which directors had the highest production value for that genre. Our analysis showed that the Sci-Fi genre had the highest profits and ceiling for revenue. Colin Trevorrow and J.A. Bayona were the most valuable directors in that genre.

## Contents
1. [Introduction](#introduction)
    - [Problem Statement](#problem_statement)
    - [Dataset](#dataset)
2. [Analysis](#analysis)
    - [Data Cleaning](#data_cleaning)
    - [Exploratory Analysis](#exploratory_analysis)
    - [Modeling](#modeling)

## Introduction <a name="introduction"></a>

### Problem Statement <a name="problem_statement"></a>
Our goal is to find the movie genre that will produce the highest profit. We also want to find which directors produce the most value within that genre.

### Dataset <a name="dataset"></a>
The analysis is based on datasets from IMDB.com (https://www.imdb.com/interfaces/) that include movies from 2010-2018. The analysis is also based off of a dataset from The-Numbers.com ([https://www.the-numbers.com/movie/budgets/all]) that includes the production budget and gross income of all movies. Our initial dataset had 146,144 entries.

## Analysis <a name="analysis"></a>

### Data Cleaning <a name="data_cleaning"></a>
We had to merge multiple dataframes in order to compare genres, directors, and revenue for each movie. We also had to drop duplicates, drop unnecessary columns, split the genre values, and create new columns before we could truly explore the data. After cleaning, our dataset had 2,123 rows and 34 columns.

### Exploratory Analysis <a name="exploratory_analysis"></a>
We found that some genres had higher average revenues than others, including Sci-Fi. We also explored which sub-genres in Sci-Fi generated the highest revenue and found that Adventure/Action was the best type of Sci-Fi. Our data also showed certain directors that produced higher values in that genre.

### Modeling <a name="modeling"></a>
Our analysis used matplotlib and seaborn to create bar charts and scatter plots to visualize the data. 


