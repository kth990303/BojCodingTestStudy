from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for cs in course:
        tmp = []
        for od in orders:
            cb = combinations(sorted(od), cs)
            tmp += cb
        ct = Counter(tmp)
        if len(ct) != 0 and max(ct.values()) != 1:
            answer += [''.join(ff) for ff in ct if 
                       ct[ff] == max(ct.values())]
    answer = sorted(answer)
    return answer