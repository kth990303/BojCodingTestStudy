from collections import defaultdict
from bisect import bisect_left

def solution(info, query):
    answer = []
    # 종류 많아봐야 16 * 3 * 2 * 2 * 2 = 384가지
    # 384 * 50000 = 19,200,000 ( O(N) 가능 )
    d = defaultdict(list)
    for t in info:
        a, b, c, e, score = t.split()
        for i in range(16):
            idx = (a if i&8 else "-", b if i&4 else "-", c if i&2 else "-", e if i&1 else "-")
            d[idx].append(int(score))

    for i in d:
        d[i].sort()

    for i in query:
        t = i.split()
        a, b, c, e, score = t[0], t[2], t[4], t[6], int(t[7])
        answer += [len(d[(a, b, c, e)]) - bisect_left(d[(a, b, c, e)], score)]

    return answer
