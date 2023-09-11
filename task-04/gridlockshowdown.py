t = int(input())

for _ in range(t):
    board = [input() for _ in range(3)]
    
    winner = None
    for player in ['X', 'O', '+']:
        for i in range(3):
            if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
                winner = player
                break
        if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
            winner = player
            break
    
    if winner:
        print(winner)
    else:
        print("DRAW")
