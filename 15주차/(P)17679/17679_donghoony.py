def solution(H, W, g):
    g = [list(x) for x in g]
    ans = 0
    def erase():
        s = set()
        for i in range(H-1):
            for j in range(W-1):
                if g[i][j] == g[i+1][j] == g[i][j+1] == g[i+1][j+1] and g[i][j] != ".":
                    s |= {(i, j), (i + 1, j), (i, j + 1), (i + 1, j + 1)}
        for y, x in s:
            g[y][x] = "."
        return len(s)

    def drop():
        for j in range(W):
            gap = 0
            for i in range(H-1, -1, -1):
                if g[i][j] == ".":
                    gap += 1
                else:
                    g[i+gap][j], g[i][j] = g[i][j], g[i+gap][j]
    while 1:
        cnt = erase()
        if cnt == 0:
            break
        ans += cnt
        drop()
    return ans
