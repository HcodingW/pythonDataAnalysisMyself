# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 00:20:20 2018

@author: Han Wu
"""
import json
path = "C:/HD_E/e-books/PythonforDataAnalysis/pydata-book-master/ch02/usagov_bitly_data2012-03-16-1331923249.txt"
records = [json.loads(line) for line in open(path)]
time_zones = [rec['tz'] for rec in records if 'tz' in rec]

def get_counts(sequence):
	counts = {}
	for x in sequence:
		if x in counts:
			counts[x] += 1
		else:
			counts[x] = 1
	return counts

counts = get_counts(time_zones)

def top_counts(count_dict, n = 10):
	pairs = [(count, tz) for tz, count in count_dict.items()]
	pairs.sort()
	return pairs[-n:]

#print(top_counts(counts))
	
from collections import Counter

counts = Counter(time_zones)
print(counts.most_common(10))
