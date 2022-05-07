#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import copy
import sys
input = sys.stdin.readline

fdx = [0, -1, -1, -1, 0, 1, 1, 1]
fdy = [-1, -1, 0, 1, 1, 1, 0, -1]
sdx = [-1, 0, 1, 0]
sdy = [0, -1, 0, 1]

m, s = map(int, input().split())
graph = [[[] for _ in range(4)] for _ in range(4)]
smell = [[0] * 4 for _ in range(4)]

for _ in range(m):
    x, y, d = map(int, input().split())
    graph[x-1][y-1].append(d-1)

shark = list(map(lambda x: int(x) - 1, input().split()))

def move():
    temp = copy.deepcopy(graph)
    res = [[[] for _ in range(4)] for _ in range(4)]
    for x in range(4):
        for y in range(4):
            while temp[x][y]:
                d = temp[x][y].pop()
                for i in range(d, d - 8, -1):
                    i %= 8
                    nx, ny = x + fdx[i], y + fdy[i]
                    if 0 <= nx < 4 and 0 <= ny < 4 and [nx, ny] != shark and smell[nx][ny] == 0:
                        res[nx][ny].append(i)
                        break
                else:
                    res[x][y].append(d)
    return res

def dfs(x, y, dep, cnt, visit):
    global eat, maxeat, shark
    if dep == 3:
        if maxeat < cnt:
            maxeat = cnt
            shark = [x, y]
            eat = visit[:]
        return
    for i in range(4):
        nx = x + sdx[i]
        ny = y + sdy[i]
        if 0 <= nx < 4 and 0 <= ny < 4:
            if [nx, ny] not in visit:
                visit.append([nx, ny])
                dfs(nx, ny, dep + 1, cnt + len(move_graph[nx][ny]), visit)
                visit.pop()
            else:
                dfs(nx, ny, dep + 1, cnt, visit)
                

for _ in range(s):
    eat = []
    maxeat = -1
    move_graph = move()
    dfs(shark[0], shark[1], 0, 0, [])
        
    for x, y in eat:
        if move_graph[x][y]:
            move_graph[x][y] = []
            smell[x][y] = 3
        
    for i in range(4):
        for j in range(4):
            if smell[i][j]: smell[i][j] -= 1
            graph[i][j] += move_graph[i][j]

answer = 0
for i in range(4):
    for j in range(4):
        answer += len(graph[i][j])

print(answer)

