#permutations: https://programmers.co.kr/learn/courses/4008/lessons/12836
#f-string: https://bluese05.tistory.com/70
#eval: https://www.w3schools.com/python/ref_func_eval.asp 

from itertools import permutations

def solution(expression):
    answer = []
    mark=["+", "-", "*"]
    per=permutations(mark)
    #use permutations function
    
    for i in per:
        #greedy?
        a1, a2 = i[0], i[1]
        tmp=[]
        listt=[]
        for j in expression.split(a1):
            #split and append to list (f string)
            tmp=[f"({k})" for k in j.split(a2)]
            listt.append(f"({a2.join(tmp)})")
            #split and append
        answer.append(abs(eval(a1.join(listt))))
    answer=max(answer)
    return answer
