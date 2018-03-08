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
mean_ratings = data.pivot_table('rating', rows='title', cols='gender', aggfunc='mean')
