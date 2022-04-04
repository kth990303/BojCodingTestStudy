import sys
input = lambda: sys.stdin.readline().rstrip()
mis = lambda: map(int, input().split())

def check_score(board: list):
    ret = 0
    remove_row = []
    for i in range(5, 1, -1):
        if sum(board[i]) == 4:
            remove_row.append(i)
            ret += 1
    for r in remove_row:
        board.pop(r)
    board = [[0] * 4 for _ in range(len(remove_row))] + board[:]
    cnt = (sum(board[0]) != 0) + (sum(board[1]) != 0)
    if cnt:
        board = [[0] * 4 for _ in range(cnt)] + board[:-cnt]
    return board, ret

def drop_block(board, pos):
    # pos : list with block position column (1, 1), (2, 3), (1), etc
    r = 0
    if len(pos) == 1:
        c = pos[0]
        for i in range(6):
            if not board[i][c]:
                r = i
            else:
                break
        board[r][c] = 1
        return board

    if pos[0] == pos[1]:
        c = pos[0]
        for i in range(5):
            if board[i][c] == board[i+1][c] == 0:
                r = i
            else:
                break
        board[r][c] = board[r+1][c] = 1
        return board
    else:
        c1, c2 = pos
        for i in range(6):
            if board[i][c1] == board[i][c2] == 0:
                r = i
            else:
                break
        board[r][c1] = board[r][c2] = 1
        return board

def drop(gboard, bboard, blocks):
    green_blocks = [x[1] for x in blocks]
    blue_blocks = [x[1] for x in rotate(*blocks)]
    gboard = drop_block(gboard, green_blocks)
    bboard = drop_block(bboard, blue_blocks)
    gboard, p1 = check_score(gboard)
    bboard, p2 = check_score(bboard)
    return gboard, bboard, p1+p2

def make_block(c, row, col):
    match c:
        case 1:
            return ((row, col),)
        case 2:
            return ((row, col), (row, col+1))
        case 3:
            return ((row, col), (row+1, col))

g = [[0] * 4 for _ in range(6)]
b = [[0] * 4 for _ in range(6)]
rotate = lambda *a: [(k[1], 3-k[0]) for k in a]

N = int(input())
ans = 0
for _ in range(N):
    blocks = make_block(*mis())
    g, b, score = drop(g, b, blocks)
    ans += score
print(ans, sum(map(sum, g)) + sum(map(sum, b)), sep='\n')