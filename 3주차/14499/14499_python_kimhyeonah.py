#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
input = sys.stdin.readline
def spin(cmd):
    temp = dice
    if cmd == 1:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = temp[3], temp[1], temp[0], temp[5], temp[4], temp[2]
    elif cmd == 2:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = temp[2], temp[1], temp[5], temp[0], temp[4], temp[3]
    elif cmd == 3:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = temp[4], temp[0], temp[2], temp[3], temp[5], temp[1]
    else:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = temp[1], temp[5], temp[2], temp[3], temp[0], temp[4]
        
n, m, x, y, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
cmd = list(map(int, input().split()))
dice = [0, 0, 0, 0, 0, 0]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for i in cmd:
    px = dx[i-1] + x
    py = dy[i-1] + y
    if 0 <= px < n and 0 <= py < m:
        spin(i)
        x, y = px, py
        if graph[px][py]:
            dice[-1] = graph[px][py]
            graph[px][py] = 0
        else:
            graph[px][py] = dice[-1]
        print(dice[0])

