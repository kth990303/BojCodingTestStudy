import sys
input = lambda: sys.stdin.readline().rstrip()
mis = lambda: map(int, input().split())

from collections import deque
N, K = mis()
belt = deque([[i, 0] for i in mis()])

zero_count = 0
def rotate():
    belt.rotate(1)
    belt[N-1][1] = 0

def move():
    global zero_count
    for i in range(N-1, 0, -1):
        if not belt[i][0] or belt[i][1] or not belt[i-1][1]: continue
        belt[i][0] -= 1
        if not belt[i][0]:
            zero_count += 1
        belt[i][1] += 1
        belt[i-1][1] -= 1
    belt[N-1][1] = 0

def drop():
    global zero_count
    if belt[0][0]:
        belt[0][1] += 1
        belt[0][0] -= 1
        if belt[0][0] == 0:
            zero_count += 1

cnt = 0
while zero_count < K:
    cnt += 1
    rotate()
    move()
    drop()
print(cnt)
