# spotifyPractice
Performing ETL on a kaggle spotify dataset.



SIMPLIFIED: dim_genre (Minimal Version)
Schema
Columns:
- genre_key (PK)
- genre_name 
- total_tracks # total_tracks ( count )
- avg_popularity ( mean )
- avg_energy ( mean )
- avg_danceability ( mean )
- popularity_tier (Low/Medium/High) ( using numpy binning )

