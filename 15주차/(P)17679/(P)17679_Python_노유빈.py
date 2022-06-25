# 나머지 테스트 코드는 통과했지만 테스트 코드 10번 정확성 실패, 테스트 코드 2번 효율성 실패이다.




# 제거되는 블럭들을 '0' 으로 치환 후 제거한 후 값이 '0'인 블럭 위의 블럭이 대치 후 list 리턴 해주기. 제거되는 블럭이 없다면 false 리턴.

def remove(a):
    list = []
    
    # 제거될 블럭 중 가장 왼쪽위 의 블럭의 좌표를 list 에 담기.
    for i in range(0,len(a)-1):
        for j in range(0,len(a[0])-1):
            if a[i][j]==a[i+1][j] and a[i][j]==a[i][j+1] and a[i][j]==a[i+1][j+1]:
                list.append([i,j])
    
    
    # list 가 비었으면 false 리턴
    if len(list)==0:
        return False    
    
    else:
        # 비었지 않다면 그 블럭 포함 4개의 블럭 값을 '0' 으로 치환.
        for i in range(0,len(list)):
            a[list[i][0]][list[i][1]]='0'
            a[list[i][0]+1][list[i][1]]='0'
            a[list[i][0]][list[i][1]+1]='0'
            a[list[i][0]+1][list[i][1]+1]='0'
        
        # 아래 블럭의 값이 '0' 이라면 자신의 값을 '0' 으로 바꾸고 아래 블럭 값을 자신의 블럭 값으로 바꾸기.    
        for i in range(0,len(a)-1):
            for j in range(0,len(a[0])):
                if a[i+1][j] == '0':
                    a[i+1][j] = a[i][j]
                    a[i][j] = '0'
        
        # 변경된 리스트 리턴
        return a

    


def solution(m, n, board):
    
    # m:높이, n:폭
    
    answer = 0
    a = [ ]
    
    str = [ ]
    
    # board를 문자를 기준으로 나누고 리스트에 저장
    
    for i in range(0,len(board)):
        for j in range(0,len(board[i])):
            str.append(board[i][j])
        a.append(str)
        str = []
    
    # compare 함수에서 false 조건이 잘 나오지 않아 반복문으로 돌림
    for i in range(0,m*n):
        a=remove(a)
        
    
    # 값이 '0' 인 블럭이 제거된 블럭이기에 그 수를 셈.
    for i in range(0,len(a)):
        answer += a[i].count('0')
    
    
    return answer
