#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def solution(files):
    head, number = [], []
    for file in files:
        file = file.lower()
        idx = 0
        h, n = '', ''
        
        while True:
            if file[idx].isdigit(): break
            h += file[idx]
            idx += 1
        head.append(h)
        
        while True:
            if len(file) == idx or not file[idx].isdigit(): break
            n += file[idx]
            idx += 1
        number.append(int(n))
        
    files = sorted(files, key = lambda x: (head[files.index(x)], number[files.index(x)]))
    return files
        

