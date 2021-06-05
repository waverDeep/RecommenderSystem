# dataset : https://www.kaggle.com/sengzhaotoo/movielens-small
# sample : https://lsjsj92.tistory.com/568
import pandas as pd

# load dataset
# 사용자가 영화에 평점을 매긴 데이터
rating_data = pd.read_csv('./dataset/ratings.csv')
# 영화 정보
movie_data = pd.read_csv('./dataset/movies.csv')

# 불필요한 정보 제거
rating_data.drop('timestamp', axis=1, inplace=True)

# rating 정보와 movie 정보를 합침
user_movie_rating = pd.merge(rating_data, movie_data, on='movieId')

# 아이템 기반 협업 필터링 (item based collaborative filtering) 을 하려면 pivot table을 만들어야 함
# 즉 사용자 - 영화에 따른 평첨 점수 데이터로 들어가야 함
# 이를 위해서 pivot table을 사용하고 아래오 같은 데이터를 분포시킴
# - data : 영화 평점 rating
# - index : 영황 title
# - columns : userId
movie_user_rating = user_movie_rating.pivot_table('rating', index='title', columns='userId')
user_movie_rating = user_movie_rating.pivot_table('rating', index='userId', columns='title')


