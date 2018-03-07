# P.24 用pandas对时区进行计数

import json
from pandas import DataFrame, Series

path = './usagov_bitly_data2012-03-16-1331923249.txt'
records = [json.loads(line) for line in open(path)]
frame = DataFrame(records)

