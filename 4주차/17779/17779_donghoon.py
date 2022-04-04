import sys
input = lambda: sys.stdin.readline().rstrip()
mis = lambda: map(int, input().split())

N = int(input())
g = [list(mis()) for i in range(N)]

def f(x, y, d1, d2):
    ret = [0] * 5
    area = [[0] * N for _ in range(N)]
    size = -1
    col_pos = y+1
    for i in range(d1+d2+1):
        if i <= d1:
            size += 1
            col_pos -= 1
        else:
            size -= 1
            col_pos += 1
        if i <= d2:
            size += 1
        else:
            size -= 1
        ret[4] += sum(g[x+i][col_pos:col_pos+size])
        area[x+i][col_pos:col_pos+size] = [5] * size
        
    for i in range(N):
        for j in range(N):
            if area[i][j] == 5:
                continue
            if 0 <= i < x+d1 and 0 <= j <= y:
                ret[0] += g[i][j]
            elif 0 <= i <= x+d2 and y < j < N:
                ret[1] += g[i][j]
            elif x+d1 <= i < N and 0 <= j < y-d1+d2:
                ret[2] += g[i][j]
            elif x+d2 < i < N and y-d1+d2 <= j < N:
                ret[3] += g[i][j]
    return max(ret) - min(ret)

ans = float('inf')
for i in range(N-2):
    for j in range(1, N-1):
        for d1 in range(1, j+1):
            for d2 in range(1, min(N-(i+d1), N-j)):
                ans = min(ans, f(i, j, d1, d2))
print(ans)