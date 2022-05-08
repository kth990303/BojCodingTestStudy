#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
input = sys.stdin.readline

from itertools import combinations
from collections import deque

def bfs(virus, blank):
    time = [[-1]*n for _ in range(n)]
    q = deque()
    maxtime = 0
    
    for v in virus:
        q.append(v)
        time[v[0]][v[1]] = 0
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            px = x + dx[i]
            py = y + dy[i]
            if 0 <= px < n and 0 <= py < n and graph[px][py] != 1 and time[px][py] == -1:
                time[px][py] = time[x][y] + 1
                if graph[px][py] == 0:
                    blank -= 1
                    maxtime = max(maxtime, time[px][py])
                q.append([px, py])
                
    if blank == 0: return maxtime
    else: return -1

dx = [1, -1, 0, 0]    
dy = [0, 0, 1, -1]

n, m = map(int, input().split())
viruspos = []
graph = []

blank = 0
for i in range(n):
    temp = list(map(int, input().split()))
    graph.append(temp)
    blank += temp.count(0)
    
    temp = [j for j, e in enumerate(temp) if e == 2]
    for j in temp: viruspos.append([i, j])
        
virus_combi = combinations(viruspos, m)
result = []

for i in virus_combi:
    ans = bfs(i, blank)
    if ans != -1: result.append(ans)
    
print(min(result) if result else -1)

