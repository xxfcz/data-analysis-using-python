# P.22 用纯Python代码对时区进行计数

from collections import defaultdict
import json

def get_counts(seq):
    counts = defaultdict(int)
    for x in seq:
        counts[x] += 1
    return counts

path = './usagov_bitly_data2012-03-16-1331923249.txt'
records = [json.loads(line) for line in open(path)]
time_zones = [rec['tz'] for rec in records if 'tz' in rec]
counts = get_counts(time_zones)
print(counts['America/New_York'])



