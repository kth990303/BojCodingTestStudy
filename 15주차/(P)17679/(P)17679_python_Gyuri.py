def rearrange(m,n,board):
    result = []
    bingo = [[(i,j), (i+1,j), (i, j+1), (i+1, j+1)] for i in range(m-1) for j in range(n-1) if board[i][j] and (board[i][j] == board[i+1][j]) and (board[i][j] == board[i][j+1]) and (board[i][j] == board[i+1][j+1])]
    for section in bingo:
        result +=section
    result = list(set(result))
    for x, y in result:
        board[x][y] = 0
    for j in range(n):
        for i in range(m-1, 0, -1):
            if not board[i][j]:
                for k in range(i-1, -1, -1):
                    if board[k][j]:
                        board[i][j], board[k][j] = board[k][j], board[i][j]
                        break
        
    return board

def solution(m, n, board):
    splitedBoard = []
    for row in board:
        splitedBoard.append([c for c in row])
    board = splitedBoard
    answer = 0
    while True:
        count = 0
        board = rearrange(m,n,board)
        for row in board:
            count += row.count(0)
        if count == answer:
            break
        else:
            answer = count
    return answer
