# # Add popularity tier (numpy binning)


# dim_genre['popularity_tier'] = pd.cut(
#     dim_genre['avg_popularity'],
#     bins=[0, 33, 66, 100],
#     labels=['Low', 'Medium', 'High']


import pandas as pd


#git sucks
df = pd.read_csv('data/dataset.csv')
# Column            Non-Null Count   Dtype
# ---  ------            --------------   -----
#  0   Unnamed: 0        114000 non-null  int64
#  1   track_id          114000 non-null  object
#  2   artists           113999 non-null  object
#  3   album_name        113999 non-null  object
#  4   track_name        113999 non-null  object
#  5   popularity        114000 non-null  int64
#  6   duration_ms       114000 non-null  int64
#  7   explicit          114000 non-null  bool
#  8   danceability      114000 non-null  float64
#  9   energy            114000 non-null  float64
#  10  key               114000 non-null  int64
#  11  loudness          114000 non-null  float64
#  12  mode              114000 non-null  int64
#  13  speechiness       114000 non-null  float64
#  14  acousticness      114000 non-null  float64
#  15  instrumentalness  114000 non-null  float64
#  16  liveness          114000 non-null  float64
#  17  valence           114000 non-null  float64
#  18  tempo             114000 non-null  float64
#  19  time_signature    114000 non-null  int64
#  20  track_genre       114000 non-null  object
# dtypes: bool(1), float64(9), int64(6), object(5)
# memory usage: 17.5+ MB

# print(list(df['track_genre'].drop_duplicates()))
#thinking of creating a dim table for each specific genres, so this involves aggregating the rows since we only have 114 genres in the whole of 114k records

dim_genre = df.groupby('track_genre').agg({
    'track_id' : 'count',
    # 'popularity' : 'mean',
    # 'duration_ms' : 'mean',
    # 'valence' : 'mean',
    # 'loudness' : 'mean',
    # 'danceability' : 'mean',
}).round(2).reset_index()


dim_genre.columns = ['genre','no_of_tracks']
dim_genre.insert(0, 'genre_id', dim_genre.index + 1)
# print(dim_genre['genre'].is_unique)  #this should return true
# dim_genre.drop_duplicates()
dim_genre.to_csv('data/dim_genre.csv', index=False)

















