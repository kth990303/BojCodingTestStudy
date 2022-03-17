from collections import deque
q = [deque(list(input())) for i in range(4)]

def spin(n, c, facing):
    if facing in 'r':
        if n < 3 and q[n][2] != q[n+1][-2]:
            spin(n+1, -c, 'r')
        q[n].rotate(c)
    if not facing:
        q[n].rotate(-c)
    if facing in 'l':
        if n > 0 and q[n][-2] != q[n-1][2]:
            spin(n-1, -c, 'l')
        q[n].rotate(c)


T = int(input())
for _ in range(T):
    N, r = map(int, input().split())
    spin(N-1, r, '')
ans = 0
for i in range(4):
    ans += (q[i][0] == '1') * 2**i
print(ans)