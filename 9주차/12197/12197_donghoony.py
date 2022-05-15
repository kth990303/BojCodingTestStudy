import sys
input = sys.stdin.readline

def tetromino(t, r):
    blocks = [
        [],

        [[1, 0],
         [1, 1],
         [0, 1]],

        [[0, 1],
         [1, 1],
         [1, 0]],

        [[1, 0],
         [1, 0],
         [1, 1]],

        [[0, 1],
         [0, 1],
         [1, 1]],

        [[1, 1],
         [1, 1]],

        [[1],
         [1],
         [1],
         [1]],

        [[0, 1, 0],
         [1, 1, 1]]
    ]
    
    ret = blocks[t]
    for i in range(r):
        rotate = [[0] * len(ret) for _ in range(len(ret[0]))]
        for y in range(len(ret)):
            for x in range(len(ret[0])):
                rotate[len(ret[0])-x-1][y] = ret[y][x]
        ret = rotate
    return ret

def solve():
    def drop(t, r, x):
        nonlocal g
        block = tetromino(t, r)
        drop_row = -1
        for row in range(H-len(block)+1):
            flag = True
            for ypos in range(len(block)):
                for xpos in range(len(block[0])):
                    if block[ypos][xpos] and g[row+ypos][x+xpos] == "x":
                        flag = False
            if flag:
                drop_row = row
            else:
                break

        if drop_row == -1:
            return False
        for ypos in range(len(block)):
            for xpos in range(len(block[0])):
                if block[ypos][xpos]:
                    g[drop_row+ypos][x+xpos] = "x"
        return True


    def clear_line():
        nonlocal g
        clear_row = []
        for i in range(H):
            if g[i].count("x") == W:
                clear_row += [i]
        for row in clear_row[::-1]:
            del g[row]
        g = [['.'] * W for _ in range(len(clear_row))] + g

    W, H, N = map(int, input().split())
    g = [['.'] * W for _ in range(H)]
    f = True
    blocks = [map(int, input().split()) for _ in range(N)]
    for i in range(N):
        t, r, x = blocks[i]
        f = drop(t, r, x)
        if not f:
            break
        clear_line()
    if f:
        for i in g:
            print(*i, sep="")
    else:
        print("Game Over!")

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        print(f"Case #{_+1}:")
        solve()
