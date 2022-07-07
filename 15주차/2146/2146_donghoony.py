import sys
input = lambda: sys.stdin.readline().rstrip()
mis = lambda: map(int, input().split())

from collections import deque

N = int(input())
g = [list(mis()) for _ in range(N)]

dy = 1, -1, 0, 0
dx = 0, 0, 1, -1
island_queue_list = []
v = [[0] * N for _ in range(N)]
c = [[0] * N for _ in range(N)]

def fill(y, x, color):
    # returns adjacent sea coordinates
    ret = deque()
    stk = [(y, x)]
    while stk:
        y, x = stk.pop()
        c[y][x] = color
        for i in range(4):
            ty, tx = y + dy[i], x + dx[i]
            if not (0 <= ty < N and 0 <= tx < N): continue
            if c[ty][tx]: continue
            if g[ty][tx] == 0:
                ret.append((ty, tx))
            else:
                stk.append((ty, tx))
    return ret

def bfs(q: deque, island_number):
    v = [[0] * N for _ in range(N)]
    for y, x in q:
        v[y][x] = 1
    while q:
        y, x = q.popleft()
        for i in range(4):
            ty, tx = y + dy[i], x + dx[i]
            if not (0 <= ty < N and 0 <= tx < N): continue
            if v[ty][tx]: continue
            if g[ty][tx] == 0:
                q.append((ty, tx))
                v[ty][tx] = v[y][x] + 1
            if g[ty][tx] == 1 and c[ty][tx] != island_number:
                return v[y][x]

cnt = 1
for i in range(N):
    for j in range(N):
        if g[i][j] == 1 and not c[i][j]:
            island_queue_list.append(fill(i, j, cnt))
            cnt += 1

ans = float('inf')
for i in range(len(island_queue_list)):
    ans = min(ans, bfs(island_queue_list[i], i+1))
print(ans)
