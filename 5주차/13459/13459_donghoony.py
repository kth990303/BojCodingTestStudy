import sys
input = lambda: sys.stdin.readline().rstrip()
mis = lambda: map(int, input().split())

g = []
H, W = mis()
marbles = [[-1, -1], [-1, -1]]
RED = 0; BLUE = 1
for i in range(H):
    t = list(input())
    if "R" in t:
        marbles[RED] = (i, t.index("R"))
    if "B" in t:
        marbles[BLUE] = (i, t.index("B"))
    g.append(t)

from collections import deque, defaultdict
dy, dx = (1, -1, 0, 0), (0, 0, 1, -1)
def bfs(r, b):
    q = deque([(*r, *b)])
    v = defaultdict(int)
    v[(*r, *b)] = 1
    cnt = 0
    while q:
        for _ in range(len(q)):
            ry, rx, by, bx = q.popleft()
            if cnt > 10:
                print(0)
                return
            if g[ry][rx] == "O":
                print(1)
                return
            for i in range(4):

                rty, rtx = ry, rx
                while 1:
                    rty += dy[i]; rtx += dx[i]
                    if g[rty][rtx] == "#":
                        rty -= dy[i]; rtx -= dx[i]
                        break
                    if g[rty][rtx] == "O":
                        break

                bty, btx = by, bx
                while 1:
                    bty += dy[i]; btx += dx[i]
                    if g[bty][btx] == "#":
                        bty -= dy[i]; btx -= dx[i]
                        break
                    if g[bty][btx] == "O":
                        break

                if g[bty][btx] == "O": # ignore blue in hole
                    continue

                if rty == bty and rtx == btx:
                    if abs(rty-ry) + abs(rtx-rx) > abs(bty-by) + abs(btx-bx):
                        rty -= dy[i]; rtx -= dx[i]
                    else:
                        bty -= dy[i]; btx -= dx[i]

                if v[(rty, rtx, bty, btx)]: continue
                q.append((rty, rtx, bty, btx))
                v[(rty, rtx, bty, btx)] = 1
        cnt += 1
    print(0)
bfs(marbles[0], marbles[1])
