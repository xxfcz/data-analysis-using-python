## P.30 对 MovieLens 1M 数据集进行切片切块

import pandas as pd

unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
users = pd.read_table('ml-1m/users.dat', sep='::', header=None, names=unames, engine='python')

rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table('ml-1m/ratings.dat', sep='::', header=None, names=rnames, engine='python')

mnames = ['movie_id', 'title', 'genres']
movies = pd.read_table('ml-1m/movies.dat', sep='::', header=None, names=mnames, engine='python')

# 合并三个表
data = pd.merge(pd.merge(ratings, users), movies)

# 按性别计算每部电影的平均得分
mean_ratings = data.pivot_table('rating', index='title', columns='gender', aggfunc='mean')

# 过滤掉评分数据不够250条的电影
ratings_by_title = data.groupby('title').size()
active_titles = ratings_by_title.index[ratings_by_title >= 250]
mean_ratings = mean_ratings.ix[active_titles]


# 女性观众最喜欢的电影
top_female_ratings = mean_ratings.sort_values(by='F', ascending=False)

# 男性和女性观众分歧最大的电影
mean_ratings['diff'] = mean_ratings['M'] - mean_ratings['F']
sorted_by_diff = mean_ratings.sort_values(by='diff', ascending=False)
