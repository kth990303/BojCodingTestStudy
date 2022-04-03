#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
input = sys.stdin.readline
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
result = []

def d(x, y, d1, d2):
    people = [0, 0, 0, 0, 0]
    tmp = [[0]*(n+1) for _ in range(n+1)]
    
    for i in range(d1+1):
        tmp[x+i][y-i] = 5
        tmp[x+d2+i][y+d2-i] = 5
    for i in range(d2+1):
        tmp[x+i][y+i] = 5
        tmp[x+d1+i][y-d1+i] = 5
    for i in range(x+1, x+d1+d2):
        five = False
        for j in range(n):
            if tmp[i][j] == 5: five = not five
            if five: tmp[i][j] = 5            
    for i in range(n):
        for j in range(n):
            if i < x+d1 and j <= y and tmp[i][j] == 0: people[0] += graph[i][j]
            elif i <= x+d2 and y < j and tmp[i][j] == 0: people[1] += graph[i][j]
            elif x + d1 <= i and j < y - d1 + d2 and tmp[i][j] == 0: people[2] += graph[i][j]
            elif x + d2 < i and y - d1 + d2 <= j and tmp[i][j] == 0: people[3] += graph[i][j]
            elif tmp[i][j] == 5: people[4] += graph[i][j]
                
    return (max(people)-min(people))
for x in range(n):
    for y in range(n):
        for d1 in range(n):
            for d2 in range(n):
                if 0<=x<=x+d1+d2<=n-1 and 0<=y-d1<y<y+d2<=n-1:
                    result.append(d(x, y, d1, d2))
print(min(result))

