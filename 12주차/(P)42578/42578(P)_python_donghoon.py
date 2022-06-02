from collections import Counter
from math import prod
def solution(clothes):
    return prod([x+1 for x in Counter([k for c, k in clothes]).values()]) - 1