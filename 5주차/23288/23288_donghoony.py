import sys
input = lambda: sys.stdin.readline().rstrip()
mis = lambda: map(int, input().split())

"""
0: upperside
  1
4 0 5 
  3
  2
"""

def rotate(dir):
    global dice
    match dir:
        case "E":
            dice = new_dice(4, 1, 5, 3, 2, 0)
        case "W":
            dice = new_dice(5, 1, 4, 3, 0, 2)
        case "N":
            dice = new_dice(3, 0, 1, 2, 4, 5)
        case "S":
            dice = new_dice(1, 2, 3, 0, 4, 5)

d = {"N":(-1, 0), "E": (0, 1), "W": (0, -1), "S": (1, 0)}
opposite_direction = lambda x: {"N":"S", "S":"N", "E":"W", "W":"E"}[x]
clockwise_direction = lambda x: {"N":"E", "E":"S", "S":"W", "W":"N"}[x]
counter_clockwise_direction = lambda x:{"N":"W", "W":"S", "S":"E", "E":"N"}[x]
def move(y, x, dir):
    global dice
    ty, tx = y + d[dir][0], x + d[dir][1]
    if not (0 <= ty < H and 0 <= tx < W):
        return move(y, x, opposite_direction(dir))
    rotate(dir)
    num = g[ty][tx]
    if dice[2] > num:
        dir = clockwise_direction(dir)
    elif dice[2] < num:
        dir = counter_clockwise_direction(dir)
    return ty, tx, dir

from collections import deque
def bfs(y, x, c):
    dy, dx = (1, -1, 0, 0), (0, 0, 1, -1)
    q = deque([(y, x)])
    v = [[0] * W for _ in range(H)]
    v[y][x] = 1
    ret = 0
    while q:
        ret += 1
        y, x = q.popleft()
        for i in range(4):
            ty, tx = y + dy[i], x + dx[i]
            if not (0 <= ty < H and 0 <= tx < W):
                continue
            if v[ty][tx] or g[ty][tx] != c:
                continue
            q.append((ty, tx))
            v[ty][tx] = 1
    return ret * c

dice = [1, 2, 6, 5, 4, 3]
new_dice = lambda *a: [dice[x] for x in a]

H, W, K = mis()
g = [list(mis()) for i in range(H)]
ans = 0
y, x, dir = 0, 0, "E"
for _ in range(K):
    y, x, dir = move(y, x, dir)
    ans += bfs(y, x, g[y][x])
print(ans)