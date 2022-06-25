# 정확성은 통과했지만 효율성을 통과하지 못했다.



# 리스트 a,b 비교 함수 (Score 제외, 조건이 일치하는 않는 것이 하나라도 있으면 False 반환 )

def compare(a,b):
    for i in range(0,len(b)):
        if b[i] not in a:
            return False
    
    return True


# Score 비교 함수

def score_compare(a,b):
    a_score = ""
    b_score = ""
    
    for i in range(0,len(a)):
        if a[i].isdigit()==True:
            a_score+=a[i]
    
    for i in range(0,len(b)):
        if b[i].isdigit()==True:
            b_score+=b[i]
    
    return int(a_score)>=int(b_score)




def solution(info, query):
    answer = 0
    
    ans = []
    
    # 2차원 리스트 초기화 
    
    a = [[]*2 for i in range(len(query))]
    
    
    # query의 각 항목들을 추출해서 리스트 a에 넣기
    
    for i in range(len(query)):
        if "cpp" in query[i]:
            a[i].append("cpp")
            
        if "java" in query[i]:
            a[i].append("java")   
            
        if "python" in query[i]:
            a[i].append("python")
            
        if "backend" in query[i]:
            a[i].append("backend")    
            
        if "frontend" in query[i]:
            a[i].append("frontend")
            
        if "junior" in query[i]:
            a[i].append("junior")    
            
        if "senior" in query[i]:
            a[i].append("senior")
            
        if "chicken" in query[i]:
            a[i].append("chicken") 
            
        if "pizza" in query[i]:
            a[i].append("pizza")     
        
    
    
    # compare 함수를 이용해서 조건에 맞는 answer 개수 세기
    
    for i in range(0,len(a)):
        for j in range(0,len(info)):
            if compare(info[j],a[i])==True and score_compare(info[j],query[i])==True:
                answer+=1
        ans.append(answer)
        answer=0
    
    
    
    
    return ans