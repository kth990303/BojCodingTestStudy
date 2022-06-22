def solution(clothes):
    kinds = []
    for item, kind in clothes:
        kinds.append(kind);
    
    kinds = list(set(kinds))
    clothesCount = [0 for i in range(len(kinds))]
    
    for item, kind in clothes:
        if kind in kinds:
            clothesCount[kinds.index(kind)] +=1
            
    answer = 1
    
    for count in clothesCount:
        answer *= (count+1)
    return answer-1
