#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from itertools import combinations
from collections import defaultdict
import bisect
def solution(info, query):
    answer = []
    people = defaultdict(list)
    for i in info:
        i = i.split()
        key = i[:-1]
        value = i[-1]
        for j in range(5):
            for combi in combinations(key, j):
                k = ''.join(combi)
                people[k].append(int(value))
    for c in people:
        people[c].sort()
    for i in query:
        key = i.split()
        score = int(key.pop())
        key = ''.join(key)
        key = key.replace('and', '').replace(' ', '').replace('-', '')
        answer.append(len(people[key])-bisect.bisect_left(people[key], score))
            
    return answer

