import numpy as np

ROWS= 3
COLUMNS =3

def mark(row, col, player):
	board[row][col]=player

def is_valid_mark(row, col):
	return board[row][col]==0

def is_board_full():
	for r in range(ROWS):
		for c in range(COLUMNS):
			if board[r][c]==0:
				return False
	return True

def is_winning_move(player):
    if player==1:
       announcement= "Player 1 Won"
    else:
    	announcement="Player 2 Won"
				
board= np.zeros((ROWS, COLUMNS))

game_over=False

turn=0

while not game_over:
    if turn%2 ==0:
        #player 1
       row=int(input("player 1: choose row number (0-2): "))
       col=int(input("player 1: choose col number (0-2): "))
       if is_valid_mark(row,col):
          mark(row ,col ,1)
          if is_winning_move(1):
             game_over=True
       else:
           turn -=1
    else:#player 2
        row=int(input("player 2: choose row number (0-2): "))
        col=int(input("player 2: choose col number (0-2): "))
        if is_valid_mark(row,col):
           mark(row ,col ,2)
           if is_winning_move(2):
               game_over=True
        else:
            turn -=1

    turn +=1
    print(board)
    if game_over==True:
       print("GAME OVER")
