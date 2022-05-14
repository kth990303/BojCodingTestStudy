import sys
input = lambda: sys.stdin.readline().rstrip()
mis = lambda: map(int, input().split())


N = int(input())
g = [list(mis()) for i in range(N)]
init_sand = sum([sum(x) for x in g])

sand_move = [(-1, 1, 0.01), (1, 1, 0.01), (-1, 0, 0.07), (1, 0, 0.07), (-2, 0, 0.02), (2, 0, 0.02),
             (-1, -1, 0.10), (1, -1, 0.10), (0, -2, 0.05), (0, -1, -1)]
# left: y, x
# right : y, -x,
# up: x, y
# down: x, -y

def move(y, x, direction):
    match direction:
        case 0:
            sand = [x for x in sand_move]
        case 1:
            sand = [(-x[1], x[0], x[2]) for x in sand_move]
        case 2:
            sand = [(x[0], -x[1], x[2]) for x in sand_move]
        case 3:
            sand = [(x[1], x[0], x[2]) for x in sand_move]
    count = 0
    for dy, dx, r in sand:
        ty, tx = y + dy, x + dx
        if r != -1:
            count += int(g[y][x] * r)
        if 0 <= ty < N and 0 <= tx < N:
            if r == -1:
                g[ty][tx] += g[y][x] - count
            else:
                g[ty][tx] += int(g[y][x] * r)
    g[y][x] = 0

dir = []
dy4 = 0, 1, 0, -1
dx4 = -1, 0, 1, 0
amount = 1
y = x = N//2
for i in range(N*2-1):
    if i == N*2:
        amount -= 1
    for t in range(amount):
        ty, tx = y + dy4[i%4], x + dx4[i%4]
        move(ty, tx, i%4)
        y, x = ty, tx
    if i%2:
        amount += 1
print(init_sand - sum([sum(x) for x in g]))