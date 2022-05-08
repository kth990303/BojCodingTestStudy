import sys
input = lambda: sys.stdin.readline().rstrip()
mis = lambda: map(int, input().split())

from collections import deque

INF = float('inf')
dy = 0, 0, 1, -1
dx = 1, -1, 0, 0

def bfs(init_virus_coordinates):
    v = [[0] * N for _ in range(N)]

    def check():
        for i in range(N):
            for j in range(N):
                if g[i][j] == v[i][j] == 0:
                    return False
        return True

    ret = 1
    q = deque([*init_virus_coordinates])
    for y, x in init_virus_coordinates:
        v[y][x] = 1
    while q:
        y, x = q.popleft()
        for i in range(4):
            ty, tx = y + dy[i], x + dx[i]
            if not (0 <= ty < N and 0 <= tx < N):
                continue
            if v[ty][tx] or g[ty][tx] == 1:
                continue
            if g[ty][tx] == 0:
                ret = max(ret, v[y][x] + 1)
            q.append((ty, tx))
            v[ty][tx] = v[y][x] + 1
    if not check():
        return INF
    return ret - 1

N, M = mis()
g = []
virus = []
for i in range(N):
    t = list(mis())
    for j in range(N):
        if t[j] == 2:
            virus += [(i, j)]
    g.append(t)

from itertools import combinations as comb
ans = INF
for virus_combination in comb(virus, M):
    ans = min(ans, bfs(virus_combination))
print(-1 if ans == INF else ans)
