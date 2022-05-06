#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
input = sys.stdin.readline
from collections import deque
n, m, k = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
dice = [1, 2, 3, 4, 5, 6]

x, y = 0, 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
cmd, total = 0, 0

def spin(x, y):
    global cmd
    if cmd == 0: #동
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]
    elif cmd == 1: #남
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]
    elif cmd == 2: #서
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]
    else: #북
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]
    
    if dice[5] > matrix[x][y]:
        if cmd == 3: cmd = 0
        else: cmd += 1
    elif dice[5] < matrix[x][y]:
        if cmd == 0: cmd = 3
        else: cmd -= 1
            
def bfs(x, y):
    count = 1
    visited = [[0]*m for _ in range(n)]
    q = deque()
    q.append([x, y])
    while q:
        x, y = q.popleft()
        visited[x][y] = 1
        for i in range(4):
            bx, by = x + dx[i], y + dy[i]
            if bx < 0 or bx >= n or by < 0 or by >= m: continue
            if matrix[bx][by]  == matrix[x][y] and not visited[bx][by]:
                q.append([bx, by])
                visited[bx][by] = 1
                count += 1
    return count

for i in range(k):
    px = x + dx[cmd]
    py = y + dy[cmd]
    if px < 0 or px >= n or py < 0 or py >= m:
        if cmd == 0 or cmd == 1: cmd += 2
        else: cmd -= 2
        px = x + dx[cmd]
        py = y + dy[cmd]
        
    x, y = px, py
    spin(x, y)
    result = bfs(x, y)
    total += matrix[x][y]*result
    
print(total)

