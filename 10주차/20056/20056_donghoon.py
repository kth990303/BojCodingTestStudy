import sys
input = lambda: sys.stdin.readline().rstrip()
mis = lambda: map(int, input().split())

N, M, K = mis()
g = [[[] for i in range(N)] for j in range(N)]
for i in range(M):
    r, c, m, s, d = mis()
    g[r-1][c-1].append([m, s, d, 0])

dy = -1, -1, 0, 1, 1, 1, 0, -1
dx = 0, 1, 1, 1, 0, -1, -1, -1

def move():
    for i in range(N):
        for j in range(N):
            for k in range(len(g[i][j])):
                fireball = g[i][j][k]
                if fireball[3]:
                    continue
                ty, tx = i + dy[fireball[2]] * fireball[1], j + dx[fireball[2]] * fireball[1]
                ty %= N; tx %= N
                g[ty][tx].append([fireball[0], fireball[1], fireball[2], 1])
    for i in range(N):
        for j in range(N):
            for k in range(len(g[i][j])-1, -1, -1):
                if not g[i][j][k][3]:
                    del g[i][j][k]
def reset():
    for i in range(N):
        for j in range(N):
            for k in range(len(g[i][j])):
                g[i][j][k][3] = 0

def split():
    for i in range(N):
        for j in range(N):
            l = len(g[i][j])
            if l < 2:
                continue
            mm = sum([x[0] for x in g[i][j]]) // 5
            ss = sum([x[1] for x in g[i][j]]) // len(g[i][j])
            dd = sum([x[2]%2 for x in g[i][j]])
            g[i][j] = []
            if not mm:
                continue
            for k in range(4):
                if dd in (0, l):
                    g[i][j].append([mm, ss, (0, 2, 4, 6)[k], 0])
                else:
                    g[i][j].append([mm, ss, (1, 3, 5, 7)[k], 0])
def total():
    ret = 0
    for i in range(N):
        for j in range(N):
            ret += sum([x[0] for x in g[i][j]])
    return ret

for i in range(K):
    move()
    split()
    reset()
print(total())