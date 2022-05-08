#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
input = sys.stdin.readline
n, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
horse_pos = {(i, j): [] for i in range (n) for j in range(n)}
horse_info = {}
for i in range(1, k+1):
    x, y, d = map(int, input().split())
    horse_pos[(x-1, y-1)].append(i)
    horse_info[i] = [x-1, y-1, d-1]
    
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
change = [1, 0, 3, 2]

def sol():
    turn = 0
    change_direction = 0
    while True:
        turn += 1
        if turn > 1000: return -1
        for i in range(1, k+1):
            hx, hy, hd = horse_info[i]
            nx, ny, nd = hx+dx[hd], hy+dy[hd], hd
            if nx < 0 or nx >= n or ny < 0 or ny >= n or graph[nx][ny] == 2:
                nd = change[hd]
                nx, ny = hx+dx[nd], hy+dy[nd]
                if nx < 0 or nx >= n or ny < 0 or ny >= n or graph[nx][ny] == 2:
                    horse_info[i][2] = nd
                    continue
                change_direction = 1
                
            if graph[nx][ny] == 0:
                pile = horse_pos[(hx, hy)][horse_pos[(hx, hy)].index(i):]
                horse_pos[(hx, hy)] = horse_pos[(hx, hy)][:horse_pos[(hx, hy)].index(i)]
                horse_pos[(nx, ny)].extend(pile)
                if len(horse_pos[(nx, ny)]) >= 4: return turn
                for j in pile:
                    horse_info[j][0], horse_info[j][1] = nx, ny
                if change_direction == 1: 
                    horse_info[i][2] = nd
                    change_direction = 0

            elif graph[nx][ny] == 1:
                pile = horse_pos[(hx, hy)][horse_pos[(hx, hy)].index(i):]
                horse_pos[(hx, hy)] = horse_pos[(hx, hy)][:horse_pos[(hx, hy)].index(i)]
                pile.reverse()
                horse_pos[(nx, ny)].extend(pile)
                if len(horse_pos[(nx, ny)]) >= 4: return turn
                for j in pile:
                    horse_info[j][0], horse_info[j][1] = nx, ny
                if change_direction == 1: 
                    horse_info[i][2] = nd
                    change_direction = 0
print(sol())

