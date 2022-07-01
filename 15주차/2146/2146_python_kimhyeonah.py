#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from collections import deque
import sys
input = sys.stdin.readline

def checkIsland(x, y, color):
    q = deque()
    q.append([x, y])
    while q:
        px, py = q.popleft()
        for i in range(4):
            nx, ny = px + dx[i], py + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n or visited[nx][ny] or not graph[nx][ny]:
                continue
            graph[nx][ny] = color
            visited[nx][ny] = True
            q.append([nx, ny])
            
def distance(x, y):
    q = deque()
    q.append([x, y, 0])
    while q:
        px, py, cnt = q.popleft()
        if graph[px][py] and graph[px][py] != graph[x][y]:
            return cnt
        for i in range(4):
            nx, ny = px + dx[i], py + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n or visited[nx][ny] or graph[nx][ny] == graph[x][y]:
                continue
            visited[nx][ny] = True
            q.append([nx, ny, cnt+1])
    
    return 1e9
            
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

dx = 1, -1, 0, 0
dy = 0, 0, 1, -1
color = 1
            
for i in range(n):
    for j in range(n):
        if graph[i][j] and not visited[i][j]:
            visited[i][j] = True
            graph[i][j] = color
            checkIsland(i, j, color)
            color += 1
            
answer = 1e9
for i in range(n):
    for j in range(n):
        if graph[i][j]:
            visited = [[False] * n for _ in range(n)]
            answer = min(answer, distance(i, j))
            
print(answer-1)

