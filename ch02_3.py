## P.24 用pandas对时区进行计数

import json
from pandas import DataFrame, Series
from matplotlib import interactive

interactive(True)

path = './usagov_bitly_data2012-03-16-1331923249.txt'
records = [json.loads(line) for line in open(path)]
frame = DataFrame(records)
clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz==''] = 'Unknown'
tz_counts = clean_tz.value_counts()
plt = tz_counts[:10].plot(kind='barh')

