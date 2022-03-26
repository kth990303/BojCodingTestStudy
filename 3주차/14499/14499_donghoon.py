import sys
input = lambda: sys.stdin.readline().rstrip()
mis = lambda: map(int, input().split())

dice = [0] * 6
new_dice = lambda a, b, c, d, e, f: [dice[a], dice[b], dice[c], dice[d], dice[e], dice[f]]

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
        case 1:
            dice = new_dice(4, 1, 5, 3, 2, 0)
        case 2:
            dice = new_dice(5, 1, 4, 3, 0, 2)
        case 3:
            dice = new_dice(3, 0, 1, 2, 4, 5)
        case 4:
            dice = new_dice(1, 2, 3, 0, 4, 5)

dy = 0, 0, -1, 1
dx = 1, -1, 0, 0

H, W, y, x, c = map(int, input().split())
g = [list(map(int, input().split())) for i in range(H)]

for i in map(int, input().split()):
    ty, tx = y + dy[i-1], x + dx[i-1]
    if not (0 <= tx < W and 0 <= ty < H):
        continue
    rotate(i)
    if g[ty][tx] != 0:
        dice[2] = g[ty][tx]
        g[ty][tx] = 0
    else:
        g[ty][tx] = dice[2]
    y, x = ty, tx
    print(dice[0])