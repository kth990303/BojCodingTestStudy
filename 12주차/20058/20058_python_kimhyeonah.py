#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from collections import deque
import sys
input = sys.stdin.readline

def firestorm(graph, n, m):
    for i in range(0, 2**n, 2**m):
        for j in range(0, 2**n, 2**m):
            rot = [graph[k][j:j+2**m] for k in range(i, i+2**m)]
            rot = list(zip(*rot[::-1]))
            for a in range(2**m):
                for b in range(2**m):
                    graph[a+i][b+j] = rot[a][b]
    melt = []
        
    for x in range(2**n):
        for y in range(2**n):
            count = 0
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
               
                if nx < 0 or nx >= 2**n or ny < 0 or ny >= 2**n: continue
                if graph[nx][ny] > 0: count += 1
            if count < 3 and graph[x][y] != 0: melt.append([x, y])
                
    for mx, my in melt: graph[mx][my] -= 1
    return graph
        
def checkarea(graph, n):
    check = [[0]*(2**n) for _ in range(2**n)]
    sumarea = 0
    icearea = []

    for i in range(2**n):
        for j in range(2**n):
            ice = 0
            if check[i][j] or graph[i][j] == 0: continue
            q = deque()
            q.append([i, j])
            check[i][j] = 1

            while q:
                px, py = q.popleft()
                ice += 1
                sumarea += graph[px][py]

                for k in range(4):
                    nx = px + dx[k]
                    ny = py + dy[k]
                    if nx < 0 or nx >= 2**n or ny < 0 or ny >= 2**n or check[nx][ny] or graph[nx][ny] == 0 : continue
                    q.append([nx, ny])
                    check[nx][ny] = 1
            icearea.append(ice)
    print(sumarea)
    print(max(icearea)) if icearea else print(0)
        
n, q = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(2**n)]
magic = list(map(int, input().split()))

dx = 1, -1, 0, 0
dy = 0, 0, -1, 1

for m in magic:
    graph = firestorm(graph, n, m)

checkarea(graph, n)

