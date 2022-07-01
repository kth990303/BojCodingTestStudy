#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def solution(m, n, board):
    def game(m, n, board):
        pop = set()
        for i in range(1, n):
            for j in range(1, m):
                if board[i][j] == board[i-1][j] == board[i][j-1] == board[i-1][j-1] != 0:
                    pop |= set([(i, j), (i-1, j-1), (i-1, j), (i, j-1)])
                    print(pop)
        for i, j in pop:
            board[i][j] = 0
        for i, e in enumerate(board):
            zero_count = e.count(0)
            board[i] = [0]*zero_count + [alpha for alpha in e if alpha]
        return pop
    board = list(map(list, zip(*board)))
    answer = 0
    while True:
        game_pop = game(m, n, board)
        if len(game_pop) == 0: return answer
        answer += len(game_pop)

