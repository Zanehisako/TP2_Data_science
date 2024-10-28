from itertools import groupby
from unicodedata import numeric
from numpy import number
import pandas as pd
from pandas.compat.numpy.function import ndarray
df = pd.read_csv('imdb_top_1000.csv')
#print(df[:5])

#Question 1
director = df['Director'].value_counts().idxmax()
print('le director plus recurent est ',director)
director_count = df['Director'].value_counts().max()
print('le director apparu :',director_count)
film = df.loc[df['IMDB_Rating'] == df['IMDB_Rating'].max(),'Series_Title'].iloc[0]
print(film)

genres= df['Genre'].str.split(',').apply(lambda x: [item.strip().title() for item in x]).explode().unique()
print('les genres sont :',genres)
genre_dominat = df.explode('Genre')['Genre'].value_counts().idxmax()
print('le genre_dominat est : ',genre_dominat)



df['Genre'] = df['Genre'].str.split(',').apply(lambda x: [item.strip().title() for item in x])
df_exploded = df.explode('Genre')
genre_counts= df_exploded['Genre'].value_counts()

rarest_genre = genre_counts.idxmin()

print("la plus rare genre est :",rarest_genre)

#Question 2
max_rating = df["IMDB_Rating"].max()
min_rating = df["IMDB_Rating"].min()
print(f'l interval est {min_rating}:{max_rating}')
films_min_rating = df.loc[df['IMDB_Rating'] == min_rating,'Series_Title']
print('les qui ont le min rating :')
print(films_min_rating)

#Question 3
def list_str_to_int(x):
    if isinstance(x,str):
        return [int(item) for item in x.split(',')]
    else:
        return []
df['Gross_int'] = df['Gross'].apply(list_str_to_int)

df['Gross_sum']= df['Gross_int'].apply(sum)
#le film avec le max Gross
print(df.loc[df['Gross_sum'] == df['Gross_sum'].max(),'Series_Title'])
#l annee de publication avec le max gross
released_year_gross= df.groupby('Released_Year')['Gross_sum'].sum()
print('l annee avec le plus grand gross est :',released_year_gross.idxmax())

"""
df_year = df.groupby(['Released_Year','Genre']).size().reset_index()
print(df_year)
"""

#Question 4
sorted_year =df.sort_values('Released_Year',ascending=True) 
print(sorted_year['Released_Year'])

sorted_IMDB_Rating = df.sort_values(['IMDB_Rating','Runtime'],ascending=[False,True])
print(sorted_IMDB_Rating)

#Question 5
print(df['Meta_score'].describe())

print('before',df['Meta_score'])
df['Meta_score_Transform'] = df['Meta_score'].div(10)
print('after',df['Meta_score_Transform'])
df['Final_Score'] = (df['Meta_score_Transform'] + df['IMDB_Rating'])/2
print(df['Final_Score'])

best_film = df['Final_Score'].max() 
print('le meilleur film ',df.loc[df['Final_Score'] == best_film,'Series_Title'])

#Question 7

star1 = df['Star1'].value_counts().idxmax()
star2 = df['Star2'].value_counts().idxmax()
star3 = df['Star3'].value_counts().idxmax()
star4 = df['Star4'].value_counts().idxmax()
print('les starts plus frequant :')
print(star1,star2,star3,star4)

stars  = pd.concat([df[col] for col in ['Star1','Star2','Star3','Star4']])
print('le star plus frequant est : ',stars.value_counts().idxmax())
