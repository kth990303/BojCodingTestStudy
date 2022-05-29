#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from collections import Counter
from math import prod
def solution(clothes):
    return prod([x+1 for x in Counter([j for i, j in clothes]).values()])-1

