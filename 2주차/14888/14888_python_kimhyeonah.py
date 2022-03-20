#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
input = sys.stdin.readline
def dfs(idx, result):
    global plus, minus, multi, divi
    if idx == n:
        total.append(result)
        return
    
    if plus > 0:
        plus -= 1
        dfs(idx+1, result+arr[idx])
        plus += 1
    if minus > 0:
        minus -= 1
        dfs(idx+1, result-arr[idx])
        minus += 1
    if multi > 0:
        multi -= 1
        dfs(idx+1, result*arr[idx])
        multi += 1
    if divi > 0:
        divi -= 1
        dfs(idx+1, int(result/arr[idx]))
        divi += 1
            
n = int(input())
arr = list(map(int, input().split()))
plus, minus, multi, divi = map(int, input().split())
total = []

dfs(1, arr[0])
print(max(total))
print(min(total))

