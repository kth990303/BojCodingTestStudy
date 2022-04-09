#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
input = sys.stdin.readline
from collections import deque, defaultdict
n, m = map(int, input().split())
marbles = [[0, 0], [0, 0]]
matrix = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
           
for i in range(n):
    row = list(input())
    if "R" in row:
        marbles[0] = [i, row.index("R")]
    if "B" in row:
        marbles[1] = [i, row.index("B")]
    matrix.append(row)


def move(rx, ry, bx, by, i):
    rcount, bcount = 0, 0
    while True:
        nrx, nry = rx+dx[i], ry+dy[i]
        if matrix[nrx][nry] == '#': break
        rx, ry = nrx, nry
        if matrix[nrx][nry] == 'O': break
        rcount += 1
    
    while True:
        nbx, nby = bx+dx[i], by+dy[i]
        if matrix[nbx][nby] == '#': break
        bx, by = nbx, nby
        if matrix[nbx][nby] == 'O': break
        bcount += 1
    
    if rx == bx and ry == by:
        if matrix[rx][ry] == 'O': return rx, ry, bx, by
        if rcount < bcount:
            bx, by = bx-dx[i], by-dy[i]
        else:
            rx, ry = rx-dx[i], ry-dy[i]
            
    return rx, ry, bx, by

def bfs(red, blue):
    visited = defaultdict(int)
    visited[(*red, *blue)] = 1
    q = deque()
    q.append((*red, *blue, 0))
    while q:
        rx, ry, bx, by, count = q.popleft()
        if count > 10:
            print(0)
            return
        
        if matrix[rx][ry] == 'O':
            print(1)
            return
        
        for i in range(4):
            prx, pry, pbx, pby = move(rx, ry, bx, by, i)
            if matrix[pbx][pby] == 'O': continue
            if visited[(prx, pry, pbx, pby)] == 0:
                q.append((prx, pry, pbx, pby, count+1))
                visited[(prx, pry, pbx, pby)] = 1
    print(0)
bfs(marbles[0], marbles[1])

