#테스트 실패 코드
#이지영

def disappear(m,n,board):
    #check the value of 2X2 blocks
    arr=[]
    for i in range(m):
        for j in range(n):
            if i+1<m and j+1<n and board[i][j] != '0' and (board[i][j] == 
            board[i][j+1] == board[i+1][j] == board[i+1][j+1]):
                arr.append([i,j])
    return arr

def drop(board, arr):
    #1. remove 2X2 blocks 
    #2. and drop others
    
    #1.
    for i, j in arr:
        board[i][j] = "0"
        
    #2.
    board = list(zip(*board)) #transpose
    for i, x in enumerate(board):
        n = x.count('0')
        board[i] = n*'0' + ''.join(x).replace('0', '')
    return list(zip(*board))
    

def solution(m, n, board):
    board = [list(i) for i in board]    
    #array to list
    answer = 0
    
    while True:
        arr=disappear(m, n, board)
        if arr == []:
            return answer
        else:
            answer += len(disappear(m, n, board))
            board = list(map(list, board))
            drop(board, arr)
    return answer
