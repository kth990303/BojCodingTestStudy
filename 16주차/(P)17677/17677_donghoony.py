from collections import Counter
# N <= 1,000이므로 O(N^2) 가능, O(N) 풀이
# f는 s가 모두 알파벳으로 이루어졌는지 확인합니다
f = lambda s: all([x.isalpha() for x in s])
# Counter는 개수를 세어 주는 multiset 개념입니다
def solution(a, b):
    a = a.lower(); b = b.lower()
    a_str = Counter([a[i:i+2] for i in range(len(a)-1) if f(a[i:i+2])])
    b_str = Counter([b[i:i+2] for i in range(len(b)-1) if f(b[i:i+2])])
    if not a_str and not b_str: return 65536
    return int(65536 * (sum((a_str & b_str).values())/sum((a_str | b_str).values())))
