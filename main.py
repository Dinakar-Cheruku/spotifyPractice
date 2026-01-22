# import pandas as pd
# import numpy as np
#
# # Load data
# df = pd.read_csv('data/spotify_data.csv')
#
# # Basic cleaning
# df = df.drop_duplicates()
#
# # Create simple dim_genre
# dim_genre = df.groupby('track_genre').agg({
#     'track_id': 'count',      # total_tracks
#     'popularity': 'mean',      # avg_popularity
#     'energy': 'mean',          # avg_energy
#     'danceability': 'mean'     # avg_danceability
# }).reset_index()
#
# # Rename columns
# dim_genre.columns = ['genre_name', 'total_tracks', 'avg_popularity',
#                      'avg_energy', 'avg_danceability']
#
# # Add popularity tier (numpy binning)
# dim_genre['popularity_tier'] = pd.cut(
#     dim_genre['avg_popularity'],
#     bins=[0, 33, 66, 100],
#     labels=['Low', 'Medium', 'High']
# )
#
# # Add surrogate key
# dim_genre.insert(0, 'genre_key', range(1, len(dim_genre) + 1))
#
# # Create fact table with FK
# fact_tracks = df.merge(
#     dim_genre[['genre_key', 'genre_name']],
#     left_on='track_genre',
#     right_on='genre_name',
#     how='left'
# ).drop('genre_name', axis=1)
#
# # Save
# dim_genre.to_csv('dim_genre.csv', index=False)
# fact_tracks.to_csv('fact_tracks.csv', index=False)
#
# print(dim_genre.head(10))
import pandas as pd

import numpy as np
























