import numpy as np
import pandas as pd
from pandas import Series,DataFrame
import json

path = 'usagov_bitly_data2012-03-16-1331923249.txt'
records = [json.loads(line) for line in open(path) if line]
frame = pd.DataFrame(records)
tz = frame.tz
tz.fillna('Missing', inplace=True)
# tz[tz=='] = 'Unknown' 会报警：SettingWithCopyWarning
frame.loc[tz=='', 'tz'] = 'Unknown'

frame.a.fillna('Missing', inplace=True)
os = np.where(frame['a'].str.contains('Windows'), 'Windows', 'Non Windows')
frame['os'] = os

# 根据tz、os列分组、计数、转换为交叉表形式
agg_counts = frame.groupby(['tz', 'os']).size().unstack()
# 按时区汇总，取最常出现的时区
subset = agg_counts.sum(1).nlargest(10)

# 绘图
import seaborn as sns
sns.barplot(x=subset.index, y=subset.values)
