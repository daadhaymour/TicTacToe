#global variables

board = ["-","-","-",
         "-","-","-",
         "-","-","-"]
currentPlayer = "x"
winner = None
gameRunning = True

#creating game board

def printBoard(board):
    print(board[0] +" | " + board[1] +" | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | "+ board[5])
    print("----------")
    print(board[6] +" | "+ board[7]+ " | "+board[8])

printBoard(board)

#take player input
def playerInput(board):
    inp = int(input("Choose a number 1-9: "))
    if inp >= 1 and inp <= 9 and board[inp-1] == "-":
        board[inp-1] = currentPlayer
    else:
        print("Invalid Input")
#check for win or tie

# switch player

#check for player 2 win/tie