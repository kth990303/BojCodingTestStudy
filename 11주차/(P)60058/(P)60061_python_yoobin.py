# 실패 : '기둥은 기둥, 보, 바닥 접해야 함 , 보는 기둥과 접하거나 보 사이에 위치해야 함' 이라는 조건을 만족시키는 알고리즘을 구현하지 못했다. 그래서 답보다 여러 개의 결과값들이 나온다. 


def remove(a):
    
    for i in range(0,len(a)-1):
        if a[i][0:3] == a[i+1][0:3]:   
            del a[i]
            del a[i]
            break
    return a


def solution(n, a):
    answer = []
    
    
    # 기둥 : 기둥, 보, 바닥 접해야 함
    # 보 : 기둥과 접하거나 보 사이에 위치
    # a는 구조물의 종류를 나타내며, 0은 기둥, 1은 보를 나타냅니다.
    # b는 구조물을 설치할 지, 혹은 삭제할 지를 나타내며 0은 삭제, 1은 설치를 나타냅니다.
    # 보는 오른쪽, 기둥은 위쪽 방향으로 설치
    
    a.sort()
    
    
    
    # 삭제 미리 해주기
    
    
    while True:        
        if len(a)==len(remove(a)):
            break
        else:
            a = remove(a)
            
    
    for i in range(0,len(a)): # 설치
              
        # 기둥
        if a[i][2]==0:         
            answer.append(a[i][0:3])
            
                
        # 보
        else:         
            answer.append(a[i][0:3])
            a[i][0] += 1
            answer.append(a[i][0:3]) 
            
            
            
            
    
    
    
    return answer