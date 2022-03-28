#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
input = sys.stdin.readline

def up(graph):
    for j in range(n):
        last = 0 #더해줄 지난 칸 값
        pos = 0 #채울 수 있는 행 위치
        for i in range(n):
            if graph[i][j]:
                if last == graph[i][j]:
                    graph[pos-1][j] = last*2
                    graph[i][j] = 0
                    last = 0
                else:
                    temp = graph[i][j]
                    graph[i][j] = 0
                    graph[pos][j] = temp
                    last = temp
                    pos += 1         
    return graph
                    
def down(graph):
    for j in range(n):
        last = 0 #더해줄 지난 칸 값
        pos = n-1 #채울 수 있는 행 위치
        for i in range(n-1, -1, -1):
            if graph[i][j]:
                if last == graph[i][j]:
                    graph[pos+1][j] = last*2
                    graph[i][j] = 0
                    last = 0
                else:
                    temp = graph[i][j]
                    graph[i][j] = 0
                    graph[pos][j] = temp
                    last = temp
                    pos -= 1          
    return graph
                
def left(graph):
    for i in range(n):
        last = 0 #더해줄 지난 칸 값
        pos = 0 #채울 수 있는 열 위치
        for j in range(n):
            if graph[i][j]:
                if last == graph[i][j]:
                    graph[i][pos-1] = last*2
                    graph[i][j] = 0
                    last = 0
                else:
                    temp = graph[i][j]
                    graph[i][j] = 0
                    graph[i][pos] = temp
                    last = temp
                    pos += 1         
    return graph
                
def right(graph):
    for i in range(n):
        last = 0 #더해줄 지난 칸 값
        pos = n-1 #채울 수 있는 열 위치
        for j in range(n-1, -1, -1):
            if graph[i][j]:
                if last == graph[i][j]:
                    graph[i][pos+1] = last*2
                    graph[i][j] = 0
                    last = 0
                else:
                    temp = graph[i][j]
                    graph[i][j] = 0
                    graph[i][pos] = temp
                    last = temp
                    pos -= 1           
    return graph
                    
def dfs(count, graph):
    global result
    if count == 5:
        result = max(result, max(map(max, graph)))
        return
    
    f = [up, down, left, right]
    for func in f:
        dfs(count+1, func([[k for k in p] for p in graph]))

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
result = 0

dfs(0, graph)
print(result)

