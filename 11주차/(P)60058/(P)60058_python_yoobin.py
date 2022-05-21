# 괄호 변환 : 실패, 거의 다 했다고 생각을 했는데 u[0] 값이 한 개가 아닌 복수 값이 나오며 제대로 되지 않았다. split 함수에서 return 값에 문제가 있던 것 같다.


# 올바른 문자열인지 check 하는 함수

def correct(u):
    a=0
    for i in range(0,len(u)):
        if u[i]=="(":
            a+=1
            if a<0:
                return False
        else:
            a-=1
            if a<0:
                return False

            
# u,v 로 나누어 주는 함수

def split(p):
    u = [ ]
    
    count = 0
    
    u.append(p[0])
    
    for i in range(1,len(p)):
        if u.count('(') == u.count(')'):
            break
        else:
            u.append(p[i])
            count += 1
    
    return count
            


def solution(p):
    answer = ""
    
    
    # 1. 입력이 빈 문자열인 경우
    
    if p == "":
        return ""
    
    
    
    # 2. u, v 로 분리 후 값 대입
    
    
    u = p[0:split(p)+1]
    v = p[split(p)+1:]
    
    
    
    # 3. u가 올바른 괄호 문자열인 경우.
    
    if correct(u)!=False:
        return u+solution(v)
        
        
        
        
    # 4. u가 올바른 괄호 문자열이 아닌 상황.
    answer = "("
    v = solution(v)
    answer += v
    answer += ")"
    
    
    
    
    return answer