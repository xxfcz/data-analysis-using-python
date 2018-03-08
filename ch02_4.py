## P.27 区分Windows用户和非Windows用户

import json
from pandas import DataFrame, Series
from matplotlib import interactive
import numpy as np

interactive(True)

path = './usagov_bitly_data2012-03-16-1331923249.txt'
records = [json.loads(line) for line in open(path)]
frame = DataFrame(records)
# 移除agent缺失的数据行
cframe = frame[frame.a.notnull()]
# 根据a值计算各行是不是Windows
os = np.where(cframe.a.str.contains('Windows'), 'Windows', 'Not Windows')
# 按时区分组
by_tz_os = cframe.groupby(['tz', os])
# 对分组结果进行计数，并重塑
agg_counts = by_tz_os.size().unstack().fillna(0)
# 构造间接索引数组，用于按升序排列
indexer = agg_counts.sum(1).argsort()
# 截到最后10行
count_subset = agg_counts.take(indexer)[-10:]
# 生成堆积条形图
count_subset.plot(kind='barh', stacked=True)
# 规范化后再绘图
normed_subset = count_subset.div(count_subset.sum(1),axis=0)
normed_subset.plot(kind='barh', stacked=True)

