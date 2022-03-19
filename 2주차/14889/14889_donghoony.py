from itertools import combinations as c
N = int(input())
arr = [list(map(int, input().split())) for i in range(N)]
teams = list(c(range(N), N//2))

def f(a):
    ret = 0
    for i in range(len(a)-1):
        for j in range(i+1, len(a)):
           ret += arr[a[i]][a[j]] + arr[a[j]][a[i]]
    return ret

ans = float('inf')
for i in range(len(teams)//2):
    start = teams[i]
    link = teams[-i-1]
    ans = min(ans, abs(f(start) - f(link)))
print(ans) 