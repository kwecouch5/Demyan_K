def updateBoard(board, click):
    def d(i,j):
        mine_count=0
        for i in range(click[0] - 1, click[0] + 2):
            for j in range(click[1] - 1, click[1] + 2):
                if 0 <= i < click[0] and 0 <= j < click[1] and board[i][j] == "M":
                    mine_count += 1
        if mine_count == 0:
            board[click[0]][click[1]] = 'B'
        else:
            board[click[0]][click[1]] = str(mine_count)
        for i in range(click[0] - 1, click[0] + 2):
            for j in range(click[1] - 1, click[1] + 2):
                if 0 <= i < click[0] and 0 <= j < click[1] and board[i][j] == "E":
                    d(board, [i, j])
    if board[click[0]][click[1]] == "M":
        board[click[0]][click[1]] = "X"
    else:
        d(click[0], click[1])
    return
