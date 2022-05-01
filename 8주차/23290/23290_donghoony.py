N, S = map(int, input().split())
g = [[[0]*8 for _ in range(4)] for __ in range(4)]
smell = [[0] * 4 for _ in range(4)]

dy8 = 0, -1, -1, -1, 0, 1, 1, 1
dx8 = -1, -1, 0, 1, 1, 1, 0, -1
dy4 = -1, 0, 1, 0
dx4 = 0, -1, 0, 1

for _ in range(N):
    y, x, d = map(int, input().split())
    g[y-1][x-1][d-1] += 1

y, x = map(int, input().split())
shark = [y-1, x-1]


def move_fish():
    ret = [[[0] * 8 for _ in range(4)] for __ in range(4)]
    for y in range(4):
        for x in range(4):
            for d in range(8):
                if not g[y][x][d]: continue
                f = 0
                direction = d
                ty, tx = y, x
                for i in range(9):
                    ty, tx = y + dy8[direction], x + dx8[direction]
                    if (not (0 <= ty < 4 and 0 <= tx < 4)) or smell[ty][tx] or [ty, tx] == shark:
                        direction -= 1
                        if direction < 0:
                            direction += 8
                        continue
                    else:
                        f = 1
                        break

                if f:
                    #print(f"{(y, x, d)} -> {(ty, tx, direction)}")
                    ret[ty][tx][direction] += g[y][x][d]
                else:
                    #print(f"{(y, x, d)} -> no move")
                    ret[y][x][d] += g[y][x][d]
    return ret

def move_shark():
    global shark
    max_fish_cnt = -1
    max_route = []
    v = [[0] * 4 for _ in range(4)]

    def dfs(y, x, route, fish_cnt):
        nonlocal max_fish_cnt, max_route
        global shark

        if len(route) == 3:
            if max_fish_cnt < fish_cnt:
                max_fish_cnt = fish_cnt
                max_route = [x for x in route]
            return

        if route:
            v[y][x] = 1
        for i in range(4):
            ty, tx = y + dy4[i], x + dx4[i]
            if not (0 <= ty < 4 and 0 <= tx < 4): continue
            add = (sum(g[ty][tx]) if not v[ty][tx] else 0)
            dfs(ty, tx, route + [i], fish_cnt+add)
        v[y][x] = 0

    dfs(*shark, [], 0)
    y, x = shark
    #print(shark, max_route, max_fish_cnt)
    for d in max_route:
        ty, tx = y + dy4[d], x + dx4[d]
        if sum(g[ty][tx]):
            g[ty][tx] = [0] * 8
            smell[ty][tx] = 3
        y, x = ty, tx
        shark = [ty, tx]

def reduce_smell():
    for y in range(4):
        for x in range(4):
            if smell[y][x]:
                smell[y][x] -= 1

def paste(source, dest):
    for i in range(4):
        for j in range(4):
            for d in range(8):
                dest[i][j][d] += source[i][j][d]
    return dest

def printg():
    arrow = "←↖↑↗→↘↓↙"
    for i in range(4):
        for j in range(4):
            for d in range(8):
                print(arrow[d] * g[i][j][d], end="")
            print(end=", ")
        print()
    print()

for _ in range(S):
    # 1. copy
    tg = [[[x for x in t] for t in k] for k in g]
    #2. move fish
    #printg()
    g = move_fish()
    #printg()
    #3. move shark
    move_shark()
    #printg()
    #4. reduce smell
    reduce_smell()
    #5. paste
    g = paste(tg, g)
    #printg()
    #print(shark)
    #print(*smell, sep='\n')
ans = 0
for i in range(4):
    for j in range(4):
        ans += sum(g[i][j])
print(ans)
