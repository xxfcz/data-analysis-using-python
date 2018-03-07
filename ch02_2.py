# P.22 用标准库对时区进行计数

import json
from collections import Counter

path = './usagov_bitly_data2012-03-16-1331923249.txt'
records = [json.loads(line) for line in open(path)]
time_zones = [rec['tz'] for rec in records if 'tz' in rec]
counts = Counter(time_zones)
# print(counts['America/New_York'])
print(counts.most_common(10))
