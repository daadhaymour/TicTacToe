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

#printBoard(board)

#take player input
def playerInput(board):
    inp = int(input("Choose a number 1-9: "))
    if inp >= 1 and inp <= 9 and board[inp-1] == "-":
        board[inp-1] = currentPlayer
    else:
        print("Invalid Input")
    
#check for win or tie

def check_horizontal(board):
    global winner #if winner changes in this function, it changes for the entire file
    if board[0] == board[1] == board[2] and board[1] != '-':
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[4] != '-':
        winner = board[3]
        return True
    elif board[5] == board[6] == board[7] and board[5]!='-':
        winner = board[5]
        return True
    return False
def check_vertical(board):
    global winner
    if board[0] == board[3] == board[6] and board[3] != '-':
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[4] != '-':
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[5] != '-':
        winner = board[2]
        return True
    return False

def check_across(board):
    global winner
    if board[0] == board[4] == board[8] and board[4] != '-':
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[4] != '-':
        winner = board[0]
        return True
    return False

def check_tie(board):
    for spot in board:
        if spot == '-':
            return False
    if check_horizontal(board) and check_across(board) and check_vertical(board):
        return False
    return True

        

# switch player
def switch_player(board):
    global currentPlayer
    if currentPlayer == 'x':
        currentPlayer = 'o'
    else:
        currentPlayer = 'x'





#check for player 2 win/tie
#def playerTie(board):
   
    


while gameRunning:
    check1 = check_horizontal(board)
    check2 = check_vertical(board)
    check3 = check_across(board)
    check4 = check_tie(board)

    if check1 or check2 or check3:
        print( winner,"Won the Game!!")
        gameRunning = False
    elif check4:
        print("Game resulted in a tie")
        gameRunning = False
    
    printBoard(board)
    switch_player(board)
    playerInput(board)
    
    
    

    
    

    #if check1:
       # break
    #elif check2:
        #break
    #elif check3:
     #   break
    