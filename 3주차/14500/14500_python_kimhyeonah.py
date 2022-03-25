#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
input = sys.stdin.readline
def dfs(x, y, count, sum):
    global result
    if result >= sum + (4-count)*maxval:
        return
    
    if count == 4:
        result = max(result, sum)
        return
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
            if count == 2:
                visited[nx][ny] = 1
                dfs(x, y, 3, sum+arr[nx][ny])
                visited[nx][ny] = 0
                
            visited[nx][ny] = 1
            dfs(nx, ny, count+1, sum+arr[nx][ny])
            visited[nx][ny] = 0

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
result = 0
maxval = 0

for i in arr:
    maxval = max(maxval, max(i))

for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        dfs(i, j, 1, arr[i][j])
        visited[i][j] = 0

print(result)

