# N = 20, 5번 이동, 상하좌우 -> 4^5 = 1024개의 경우의 수 완전탐색 시뮬레이션

from collections import deque
N = int(input())
g = [list(map(int, input().split())) for _ in range(N)]

def move(g, rot):
    # LRUD
    if rot in "LR":
        t = [deque([k for k in g[x] if k != 0]) for x in range(N)]
    else:
        t = [deque([k for k in list(zip(*g))[x] if k != 0]) for x in range(N)]

    retg = [[0] * N for _ in range(N)]
    for i in range(N):
        q = t[i]
        ret = []
        while q:
            if rot in "LU":
                if len(q) > 1 and q[0] == q[1]:
                    ret.append(q[0]*2)
                    q.popleft()
                    q.popleft()
                else:
                    ret.append(q[0])
                    q.popleft()
            else:
                if len(q) > 1 and q[-1] == q[-2]:
                    ret.append(q[-1] * 2)
                    q.pop()
                    q.pop()
                else:
                    ret.append(q[-1])
                    q.pop()
        if not ret:
            continue
        if rot in "LU":
            retg[i][:len(ret)] = ret
        else:
            retg[i][-len(ret):] = ret[::-1]
    if rot in "UD":
        retg = list(map(list, zip(*retg)))
    return retg

def dfs(depth, g):
    global ans
    if depth == 5:
        ans = max(ans, max(map(max, g)))
        return
    for i in "RDLU":
        dfs(depth+1, move(g, i))

ans = 0
for i in "RDLU":
    dfs(0, g)
print(ans)
