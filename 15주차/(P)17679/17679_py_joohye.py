import numpy as np
def refresh(board):
    #블록 갱신
    new_board = []
    stack = []
    tmp = []
    board = np.transpose(board)
    
    for lst in board:
        stack = []
        for j in range((lst=='0').sum()):
            stack.append('0')
        for i in lst:
            if i!='0':
                stack.append(i)
        # print(stack)
        new_board.append(stack)
    
    board = np.transpose(new_board)
    # print(board)
    return board

def check(board):
    axis = []
    for i in range(len(board)-1) :
        for j in range(len(board[i])-1):
            if(board[i][j] != '0' and board[i][j] == board[i][j+1] and board[i][j]==board[i+1][j] and board[i][j]==board[i+1][j+1]):
                axis.append([i, j])
                axis.append([i, j+1])
                axis.append([i+1, j])
                axis.append([i+1, j+1])
    #중복좌표값 제거
    new_axis = []
    for (i, j) in axis:
        if [i, j] not in new_axis:
            new_axis.append([i,j])
    #'0'으로 바꾸기
    for(i, j) in new_axis:
        board[i][j] = '0'
    
    
    return len(new_axis)

def solution(m, n, board):
    answer = 0
    lst = [x for x in board]
    board = []
    for i in range(m):
        arr = [x for x in lst[i]]
        board.append(arr)
    
    while True:
        cnt = check(board)
        if cnt == 0:
            break
        answer += cnt
        board = refresh(board)
    
    # answer+=check(board)
    # board = refresh(board)
    # answer+=check(board)
        
    
    return answer
