H, W = map(int, input().split())
g = [list(map(int, input().split())) for i in range(H)]
v = [[0] * W for i in range(H)]

max_value = max(map(max, g))
ans = 0
def dfs(y, x, block, val):
    global ans
    if block == 4:
        ans = max(ans, val)
        return

    if val + (max_value * (4-block)) < ans:
        return

    for ty, tx in ((y, x+1), (y, x-1), (y+1, x), (y-1, x)):
        if not (0 <= ty < H and 0 <= tx < W):
            continue
        if v[ty][tx]:
            continue
        if block == 2:
            v[ty][tx] = 1
            dfs(y, x, block+1, val+g[ty][tx])
            v[ty][tx] = 0
        v[ty][tx] = 1
        dfs(ty, tx, block+1, val+g[ty][tx])
        v[ty][tx] = 0

for i in range(H):
    for j in range(W):
        v[i][j] = 1
        dfs(i, j, 1, g[i][j])
        v[i][j] = 0
print(ans)