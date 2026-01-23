import pandas as pd
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker

fact_genre = pd.read_csv('data/fact_genre.csv')
df = fact_genre
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# genre_ls = fact_genre['genre']
# print(list(genre_ls))

# print(fact_genre.columns)
# for i in fact_genre.columns:
#     col_ls = fact_genre[i]
#     print(col_ls)

# print(fact_genre.info())

#   Column            Non-Null Count  Dtype
# ---  ------            --------------  -----
#  0   genre_id          114 non-null    int64
#  1   genre             114 non-null    object
#  2   popularity_desc   114 non-null    object
#  3   avg_popularity    114 non-null    float64
#  4   explicit_rate     114 non-null    float64
#  5   tempo_min         114 non-null    float64
#  6   tempo_max         114 non-null    float64
#  7   tempo_range       114 non-null    float64
#  8   avg_danceability  114 non-null    float64
#  9   danceability      114 non-null    object
#  10  no_of_tracks      114 non-null    int64


engine = create_engine('sqlite:///data/fact_genre.db')
Base = declarative_base()

class GenreStats(Base):
    __tablename__ = "genre_stats"

    genre_id = Column(Integer, primary_key=True, autoincrement=True)
    genre = Column(String)
    popularity_desc = Column(String)
    avg_popularity = Column(Float)
    explicit_rate = Column(Float)
    tempo_min = Column(Float)
    tempo_max = Column(Float)
    tempo_range = Column(Float)
    avg_danceability = Column(Float)
    danceability = Column(String)
    no_of_tracks = Column(Integer)

#this executes the above create command (kinda)
Base.metadata.create_all(engine)

#now we need to create a session for inserting the data, its like a transaction boundary, a staging area before commits

Session = sessionmaker(bind=engine)
session = Session()

columns = fact_genre.columns.tolist()
# print(columns)

# now the real task of creating a function to insert the data

# def new_genre(name):
#     genre = GenreStats(genre=name)
#     session.add(genre)
#     session.commit()
# #
# genre_ls = df['genre'].tolist()
#
# for i in genre_ls:
#     new_genre(i)
# session.close()

# print(session.query(GenreStats).all())
print(pd.read_sql("SELECT * FROM genre_stats", engine))