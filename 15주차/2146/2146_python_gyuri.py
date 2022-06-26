# 런타임 에러 (NameError)가 발생하는데 이유를 모르겠습니다 ㅠㅠ

import sys
from itertools import permutations
from itertools import combinations
from itertools import product

flag = [0 for i in range(len(vertices))]
n = int(input())
arr =[]
for _ in range(n):
    arr.append(list(map(int, input().split())))

    
vertices = [(i, j) for i, row in enumerate(arr) for j, col in enumerate(row) if arr[i][j]]
empty = [(i, j) for i, row in enumerate(arr) for j, col in enumerate(row) if not arr[i][j]]

lands = BFS(0,0,vertices)
endVertics = [[(x,y) for x, y in land if (x+1 < n and arr[x+1][y]==0) or (x-1 >=0 and arr[x-1][y]==0) or (y+1 < n and arr[x][y+1]==0) or (y-1 >= n and arr[x][y-1]==0)] for land in lands ]


landPair = list(combinations(endVertics, 2))
minDistance = []
combinations = []
for i, land in enumerate(landPair):
    dist = []
    land1 = list(land[0])
    land2 = list(land[1])
    combinations.append(list(product(land1, land2)))
    for pair in combinations[i]:
        dist.append(abs(pair[0][0] - pair[1][0]) + abs(pair[0][1] - pair[1][1])-1)
    minDistance.append((i, dist.index(min(dist)), min(dist)))
minDistance.sort(key=lambda x: x[-1])
shortPathLen = minDistance[0][2]
print(shortPathLen)

def landAttacher(x, y, vertices):
    land = []
    queue = [(x,y)]
    flag[vertices.index((x,y))] = 1
    while len(queue)!=0:
        vertex = queue.pop(0)
        land.append(vertex)
        if (vertex[0]+1, vertex[1]) in vertices and not flag[vertices.index((vertex[0]+1, vertex[1]))]:
            queue.append((vertex[0]+1, vertex[1]))
            flag[vertices.index((vertex[0]+1, vertex[1]))] = 1
        if (vertex[0], vertex[1]+1) in vertices and not flag[vertices.index((vertex[0], vertex[1]+1))]:
            queue.append((vertex[0], vertex[1]+1))
            flag[vertices.index((vertex[0], vertex[1]+1))] = 1
    return land

def BFS(x,y,vertecies):
    lands = []
    for x, y in vertecies:
        if not flag[vertecies.index((x,y))]:
            lands.append(landAttacher(x, y, vertices))
    return lands
