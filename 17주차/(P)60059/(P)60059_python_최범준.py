def rotation(array, n): #array라는 2차원 배열을 시계방향으로 90도 n번 돌리는 함수
    #시계 돌리는 알고리즘을 구현을 못하겠습니다. ... 
    array = array 
    return array 
     
def check(key, lock): #key와 lock 각 2차원 배열이 문제 조건에 통과할 수 있는지 check하는 함수 
    #통과하는 조건을 알고리즘을 구현을 못하겠습니다.. ㅜㅜ
    flag = False    
    return flag 
    

def solution(key, lock): 
    answer = False 

    for i in range(1, 5): #시계방향으로 돌려가며 확인한다. 
        new_key = rotation(key, i) 
        answer = check(new_key, lock) 
    
    return answer