import sys
input = lambda: sys.stdin.readline().rstrip()
mis = lambda: map(int, input().split())

"""
모든 P에 대해서 BFS를 진행합니다. N <= 5이므로 어떻게 해도 시간이 초과되는 일은 거의 없을 것
BFS 진행 중 거리가 2 이하이면서 P인 곳을 만나면 그 대기실은 0
맨해튼 거리는 곧 BFS상의 거리 (최단거리)
"""

from collections import deque
dy = 1, -1, 0, 0
dx = 0, 0, 1, -1

def solve(g):
    def bfs(y, x):
        v = [[-1] * 5 for i in range(5)]
        q = deque([(y, x)])
        v[y][x] = 0
        while q:
            y, x = q.popleft()
            for i in range(4):
                ty, tx = y + dy[i], x + dx[i]
                if not (0 <= ty < 5 and 0 <= tx < 5): continue
                if v[ty][tx] != -1: continue
                if g[ty][tx] == "X": continue
                if g[ty][tx] in "OP":
                    q.append((ty, tx))
                    v[ty][tx] = v[y][x] + 1
                    if g[ty][tx] == "P" and v[ty][tx] <= 2:
                        return False
        return True

    ret = 1
    for i in range(5):
        for j in range(5):
            if g[i][j] == "P":
                ret &= bfs(i, j)
                if not ret:
                    return ret
    return ret

def solution(places):
    return [solve(x) for x in places]
