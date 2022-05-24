def solution(clothes):
    answers = 1
    answer = [ ] 
    temp = ""
        
    # clothes[i][j] 를 clothes[j][i] 로 변경 -> 의상 종류대로 정렬하기 위해.
    
    for i in range(0,len(clothes)):
        temp = clothes[i][0]
        clothes[i][0] = clothes[i][1]
        clothes[i][1] = temp
        
    # clothes 를 의상을 기준으로 정렬    
    clothes.sort()
    
    count = 1
    
    # 각 의상의 종류의 수를 answer 리스트에 append
    
    for i in range(0,len(clothes)-1):
        if clothes[i][0]==clothes[i+1][0]:            
            count+=1
        else:
            answer.append(count)
            count=1
    
    # answer에 마지막 의상의 종류의 수를 append
    answer.append(len(clothes)-sum(answer))
    
    
    # answer의 원소들에 1을 더한 값들을 곱한 수를 answers 에 대입
    for i in answer:
        answers *= (i+ 1)
    
    return answers-1