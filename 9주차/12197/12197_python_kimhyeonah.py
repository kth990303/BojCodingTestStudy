#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def choose_block(typ, rotate):
    tetromino = [[], [[1, 0], [1, 1], [0, 1]], [[0, 1], [1, 1], [1, 0]], [[1, 0], [1, 0], [1, 1]], [[0, 1], [0, 1], [1, 1]],
        [[1, 1], [1, 1]], [[1], [1], [1], [1]], [[0, 1, 0], [1, 1, 1]]]
    
    choose = tetromino[typ]
    for i in range(rotate):
        choose = list(map(list, zip(*choose)))[::-1]
    return choose

def check(graph, block, h, fall):
    row = -1
    for r in range(h-len(block)+1):
        conflict = False
        for x in range(len(block)):
            for y in range(len(block[0])):
                if graph[x+r][y+fall] == 'x' and block[x][y]: 
                    conflict = True
                    break
            if conflict: break
        else: row = r
        
        if conflict: break
                
    if row == -1: return False
    
    for x in range(len(block)):
        for y in range(len(block[0])):
            if block[x][y]: graph[x+row][y+fall] = 'x'
    return True

def clear(graph, w, h):
    temp = []
    for i in range(h):
        if graph[i].count('x') == w: temp.append(i)
    for i in temp[::-1]:
        del graph[i]
    graph = [['.']*w for _ in range(len(temp))] + graph

def sol():
    w, h, n = map(int, input().split())
    graph = [['.']*w for _ in range(h)]
    blocks = [map(int, input().split()) for _ in range(n)]
    
    for typ, rotate, fall in blocks:
        block = choose_block(typ, rotate)
        if not check(graph, block, h, fall): break
        clear(graph, w, h)
    else:
        print('\n'.join(map(''.join, graph)))
        return
    print('Game Over!')
        
    
T = int(input())

for i in range(T):
    print('Case #{}:'.format(i+1))
    sol()

