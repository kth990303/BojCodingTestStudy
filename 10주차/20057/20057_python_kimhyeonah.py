#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
input = sys.stdin.readline

def sand(x, y, dir):
    global result
    
    if y < 0: return
    
    total = 0
    for dirx, diry, rate in dir:
        nx = x + dirx
        ny = y + diry
        
        if rate == 0:
            new = graph[x][y] - total
        else:
            new = int(graph[x][y]*rate)
            total += new
        
        if 0 <= nx < n and 0 <= ny < n:
            graph[nx][ny] += new
        else:
            result += new

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
x, y = n//2, n//2

left = [[-2, 0, 0.02], [-1, -1, 0.1], [-1, 0, 0.07], [-1, 1, 0.01], [0, -2, 0.05], 
        [1, -1, 0.1], [1, 0, 0.07], [1, 1, 0.01], [2, 0, 0.02], [0, -1, 0]]
right = [[x, -y, z] for x, y, z in left]
up = [[y, x, z] for x, y, z in left]
down = [[-y, x, z] for x, y, z in left]

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
dir = [left, down, right, up]
time, result = 0, 0

for i in range(2*n-1):
    if i%4 == 0 or i%4 == 2: time += 1
    for j in range(time):
        nx = x + dx[i%4]
        ny = y + dy[i%4]
        sand(nx, ny, dir[i%4])
        x, y = nx, ny
        
print(result)

