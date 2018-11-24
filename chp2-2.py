# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 11:50:09 2018

@author: Han Wu
"""

import json
path = "C:/HD_E/e-books/PythonforDataAnalysis/pydata-book-master/ch02/usagov_bitly_data2012-03-16-1331923249.txt"
records = [json.loads(line) for line in open(path)]

from pandas import DataFrame, Series
import pandas as pd; import numpy as np
frame = DataFrame(records)
#print(frame['tz'][:10])
tz_counts = frame['tz'].value_counts()
#print(tz_counts[:10])

clean_tz = frame['tz'].fillna('Missing')  #键值缺失(NA)替换成Missing
clean_tz[clean_tz == ''] = 'Unknown'      #键值为空字符串替换成Unknown
tz_counts = clean_tz.value_counts()
#print(tz_counts)
#tz_counts[:10].plot(kind = 'barh', rot = 0)

results = Series([x.split()[0] for x in frame.a.dropna()])
#print(results[:5])
#print(results.value_counts()[:10])
cframe = frame[frame.a.notnull()]   #将a字段缺失的数据项移除
operating_S = np.where(cframe['a'].str.contains('Windows'), 'Windows', 'Not Windows')
#print(operating_S[:5])
by_tz_os = cframe.groupby(['tz', operating_S])
agg_counts = by_tz_os.size().unstack().fillna(0)
#print(agg_counts[:10])
indexer = agg_counts.sum(1).argsort()
print(indexer[:10])
count_subset = agg_counts.take(indexer)[-10:]
print(count_subset)
count_subset.plot(kind = 'barh', stacked = True)
normed_subset = count_subset.div(count_subset.sum(1), axis = 0)
normed_subset.plot(kind = 'barh', stacked = True)
