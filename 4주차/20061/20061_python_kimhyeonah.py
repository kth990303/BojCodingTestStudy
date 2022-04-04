#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
input = sys.stdin.readline
from collections import deque
n = int(input())
blue = deque([[0]*6 for _ in range(4)])
green = deque([[0]*4 for _ in range(6)])
score = 0

def move_blue(t, x):
    y = 0
    if t == 1 or t == 2:
        for i in range(6):
            if blue[x][i] == 1:
                break
            y+= 1
        blue[x][y-1] = 1
        if t == 2: blue[x][y-2] = 1
    else:
        for i in range(6):
            if blue[x][i] == 1 or blue[x+1][i] == 1:
                break
            y+= 1
        blue[x][y-1] = 1
        blue[x+1][y-1] = 1
                
def move_green(t, y):
    x = 0
    if t == 1 or t == 3:
        for i in range(6):
            if green[i][y] == 1:
                break
            x += 1
        green[x-1][y] = 1
        if t == 3: green[x-2][y] = 1
    else:
        for i in range(6):
            if green[i][y] == 1 or green[i][y+1] == 1:
                break
            x += 1
        green[x-1][y] = 1
        green[x-1][y+1] = 1
                
def check():
    global blue, green, score
    bluecheck, greencheck = [], []
    
    for i in range(6):
        if sum(list(zip(*blue))[i]) == 4:
            bluecheck.append(i)
            score += 1
        
        if sum(green[i]) == 4:
            greencheck.append(i)
            score += 1
            
    for i in bluecheck:
        tmp = deque(list(map(list, zip(*blue))))
        del tmp[i]
        tmp.appendleft([0]*6)
        blue = deque(list(map(list, zip(*tmp))))
        
    for i in greencheck:
        del green[i]
        green.appendleft([0]*4)
        
    for i in range(2):
        if sum(list(zip(*blue))[i]) != 0:
            tmp = deque(list(map(list, zip(*blue))))
            del tmp[5]
            tmp.appendleft([0]*6)
            blue = deque(list(map(list, zip(*tmp))))
        if sum(green[i]) != 0:
            del green[5]
            green.appendleft([0]*4)
        
for i in range(n):
    t, x, y = map(int, input().split())
    move_blue(t, x)
    move_green(t, y)
    check()
    
print(score)
print(sum(sum(i) for i in blue) + sum(sum(i) for i in green))

