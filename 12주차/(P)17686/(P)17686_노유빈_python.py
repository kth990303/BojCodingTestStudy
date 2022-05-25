# 실패 : 몇 가지의 경우에서 답이 다르게 출력이 된다. "비교해주며 순서를 바꿔야 할 상황이 오면 a,b,c 모두 자리를 바꿔주기" 부분에서 문제가 있는데 어느 부분인지 못찾겠다.



def find_HEAD(n): # HEAD를 return 하는 함수
    head = ""
    for i in range(0,len(list(n))):
        for j in range(0,len(list(n[i]))):
            if n[i][j].isdigit()!=True:
                head += n[i][j]
            else:
                return head
            
            

def solution(files):
    answer = [ ]
    
    a = [0] * len(files) # HEAD
    b = [0] * len(files) # NUMBER
    c = [0] * len(files) # TAIL
    
    
    a1 = ""   # HEAD 변수
    b1 = ""   # NUMBER 변수
    c1 = ""   # TAIL 변수 
    
    
    # HEAD, NUMBER, TAIL 분리 후 각 값을 리스트에 대입
    
    for i in range(0,len(list(files))):                   
        a1 = find_HEAD(files[i])
        for k in range(len(list(a1)),len(list(files[i]))):
            if files[i][k].isdigit()==True:
                b1+=files[i][k]
            
        a[i]=a1
        b[i]=b1        
        c[i]=files[i][len(list(a[i]))+len(list(b[i])):]
         
        a1 = ""   # HEAD 변수 초기화
        b1 = ""    # NUMBER 변수 초기화
        c1 = ""   # TAIL 변수 초기화
        
    
    t1 = ""
    t2 = ""
    t3 = ""
    
    # 비교해주며 순서를 바꿔야 할 상황이 오면 a,b,c 모두 자리를 바꿔주기
    
    for i in range(0,len(a)-1):
        for j in range(i+1,len(a)):
            if a[i].lower()>a[j].lower():
                t1 = a[i]
                a[i] = a[j]
                a[j] = t1
                
                t2 = b[i]
                b[i] = b[j]
                b[j] = t2
                
                t3 = c[i]
                c[i] = c[j]
                c[j] = t3
            else:
                if int(b[i])>int(b[j]):
                    t1 = a[i]
                    a[i] = a[j]
                    a[j] = t1
                
                    t2 = b[i]
                    b[i] = b[j]
                    b[j] = t2
                
                    t3 = c[i]
                    c[i] = c[j]
                    c[j] = t3
                

    # answer 리스트 생성 후 값 대입
                    
    answer = [ ]
    
    for i in range(0,len(a)):
        answer.append(a[i]+b[i]+c[i])
                
    
    
    
    return answer