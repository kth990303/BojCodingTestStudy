import sys
input = lambda: sys.stdin.readline().rstrip()
mis = lambda: map(int, input().split())

def rotate(L):
    K = 2**(N-L)
    for i in range(K):
        for j in range(K):
            arr = []
            for p in range(2**L):
                t = []
                for q in range(2**L):
                    t.append(g[2**L*i+p][2**L*j+q])
                arr.append(t)
            arr = list(zip(*arr[::-1]))
            for p in range(2**L):
                for q in range(2**L):
                    g[2**L*i+p][2**L*j+q] = arr[p][q]
dy = 1, 0, -1, 0
dx = 0, 1, 0, -1
def melt():
    target = []
    for i in range(2**N):
        for j in range(2**N):
            cnt = 0
            for k in range(4):
                ty, tx = i + dy[k], j + dx[k]
                if not (0 <= ty < 2**N and 0 <= tx < 2**N): continue
                if g[ty][tx]:
                    cnt += 1
            if cnt < 3:
                target += [(i, j)]
    for y, x in target:
        if g[y][x]:
            g[y][x] -= 1

from collections import deque
def solve():
    largest_count = 0
    v = [[0] * 2**N for _ in range(2**N)]

    def bfs(y, x):
        nonlocal largest_count
        q = deque([(y, x)])
        v[y][x] = 1
        cur_count = 1
        while q:
            y, x = q.popleft()
            for i in range(4):
                ty, tx = y + dy[i], x + dx[i]
                if not (0 <= ty < 2**N and 0 <= tx < 2**N):
                    continue
                if v[ty][tx]:
                    continue
                if g[ty][tx]:
                    cur_count += 1
                    v[ty][tx] = 1
                    q.append((ty, tx))
        largest_count = max(largest_count, cur_count)

    for i in range(2**N):
        for j in range(2**N):
            if not v[i][j] and g[i][j]:
                bfs(i, j)
    return sum([sum(x) for x in g]), largest_count

N, Q = mis()
g = [list(mis()) for i in range(2**N)]
query = list(mis())
for q in query:
    rotate(q)
    melt()
print(*solve(), sep='\n')
