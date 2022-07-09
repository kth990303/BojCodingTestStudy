import math
a = 65536

def check(strr):
    strr = strr.lower()
    listt = []
    for i in range(len(strr) - 1):
        if strr[i:i + 2].isalpha():
            listt.append(strr[i:i + 2])
    return listt

def solution(str1, str2):
    s1 = check(str1)
    s2 = check(str2)
    if s1 == [] and s2 == []:
        return a

    s1_cp = s1.copy()
    s2_cp = s2.copy()

    # 교집합
    join = []
    for i in s1:
        if i in s2_cp:
            join.append(i)
            s1_cp.remove(i)
            s2_cp.remove(i)
    # 합집합
    union = join + s1_cp + s2_cp
    answer = math.floor((len(join) / len(union)) * a)
    return answer

#print(solution("FRANCE", "french"))