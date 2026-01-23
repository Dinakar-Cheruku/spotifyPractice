import numpy as np
import pandas as pd
df = pd.read_csv('data/dataset.csv')
dim_genre = pd.read_csv('data/dim_genre.csv')

dim_genre_profile = (
    df.groupby('track_genre')
      .agg(
          avg_popularity=('popularity', 'mean'),
          explicit_rate=('explicit', 'mean'),
          tempo_min=('tempo', 'min'),
          tempo_max=('tempo', 'max'),
          avg_danceability=('danceability', 'mean')
      )
      .round(2)
      .reset_index()
      .rename(columns={'track_genre': 'genre'})
)
print(dim_genre_profile.head())
dim_genre_profile.insert(0, 'genre_id', dim_genre_profile.index+1)

# print(list(dim_genre_profile.columns))

fact_genre = dim_genre_profile.merge(dim_genre, on=['genre_id','genre'],how='inner')
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
# print(fact_genre.describe())

fact_genre.insert(2,"popularity_desc",np.where(fact_genre['avg_popularity']>=50,'heavily popular genre','just another genre'))

fact_genre.insert(7,"tempo_range",(fact_genre['tempo_max']-fact_genre['tempo_min']).round(2))

fact_genre.insert(9,"danceability",np.where(fact_genre['avg_danceability']>=0.7,'Party worthy','normal danceability'))

fact_genre['explicit_rate'] = (fact_genre['explicit_rate'] * 100).round(2)

# df['genre_class'] = np.where(
#     df['avg_popularity'] >= 80,
#     'Super Popular',                 # if
#     np.where(
#         df['avg_popularity'] >= 60,
#         'Popular',                    # elif
#         np.where(
#             df['avg_popularity'] >= 40,
#             'Medium',                 # elif
#             np.where(
#                 df['avg_popularity'] >= 20,
#                 'Low',                # elif
#                 'Very Low'            # else
#             )
#         )
#     )
# )

# print(fact_genre.head())



fact_genre.to_csv('data/fact_genre.csv', index=False)


