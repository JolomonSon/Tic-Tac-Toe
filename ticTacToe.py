import time
#-------------Global Variables--------------
gameStillGoing = True#- this ensures continuity of the game
winner = None#- The current stat of the game
#currentPlayer = player#- as the name implies this container holds the currentPlayer(It's gonna be a dynamic variable tho)


#-------------------------------------------
#gameBoard - this is the format of the tic-tac-toe board
board =['-','-','-','-','-','-','-','-','-']
#displayBoard as the name inplies, shows the board
def displayBoard():
    print(board[0],'|',board[1],'|',board[2])
    print(board[3],'|',board[4],'|',board[5])
    print(board[6],'|',board[7],'|',board[8])
#handleTurn function collects the position of the players input
def handleTurn(currentPlayer):
    position = input('Choose a position from 1-9: ')
    while position not in ['1','2','3','4','5','6','7','8','9']:
        position = input('Invalid Input choose a position from 1-9: ')
    position = int(position) - 1
    board[position] = currentPlayer
    displayBoard()
    flipPlayer()
#playGame - all necessary functions and commands for the game to start, continue and finish 
def playGame():
    print('Tic-Tac-Toe')
    question = input('Hello gamer would you like to play?\n>> ')
    if (question == 'Yes' or question == 'yes' or question == 'YES'):
        global player
        player = input('Select player\nPlayer1 is X \nPlayer2 is O\n>> ')
        if player == 'X' or player == 'x':
            xPlayer = 'Hello X You are player1'
            print(xPlayer)
            print('Tic-Tac-Toe Board')
            displayBoard()
            handleTurn(player)
        elif player == 'O' or player == 'o':
            oPlayer = 'Hello O You are player2'
            print(oPlayer)
            print('Tic-Tac-Toe Board')
            displayBoard()
            handleTurn(player)
    else:
        print('You Must Play!!!')
        time.sleep(1)
        playGame()
    while gameStillGoing:
        global winner   
        handleTurn(player)
        checkBoardFull()
        if winner == 'X' or winner == 'x' or winner == 'O' or winner == 'o':
            print(winner+' won.')
        #elif winner == None:
            #print('Tie.')

#checkFullBoard function is called after each players turn to know the game current status determining the next line of action
def checkBoardFull():
    checkWin()
    #checkTie()
#checkWin - this check for a win in the game (i.e if a player has a sequence in it's order of position[row, column, diagonal]) 
def checkWin():
    global winner
    rowWinner = checkRowWin()#checkRowWin
    columnWinner = checkColumnWin()#checkColumnWin
    diagonalWinner = checkDiagonalWin()#checkDiagonalWin
    if rowWinner:
        winner = rowWinner
    elif columnWinner:
        winner = columnWinner
    elif diagonalWinner:
        winner = diagonalWinner
def checkRowWin():
    global gameStillGoing
    row1 = board[0] == board[1] == board[2] != '-'
    row2 = board[3] == board[4] == board[5] != '-'
    row3 = board[6] == board[7] == board[8] != '-'
    if row1 or row2 or row3:
        gameStillGoing = False
    if row1:
        return board[0]
    if row2:
        return board[3]
    if row3:
        return board[6]
    return
def checkColumnWin():
    global gameStillGoing
    column1 = board[0] == board[3] == board[6] != '-'
    column2 = board[1] == board[4] == board[7] != '-'
    column3 = board[2] == board[5] == board[8] != '-'
    if column1 or column2 or column3:
        gameStillGoing = False
    if column1:
        return board[0]
    if column2:
        return board[1]
    if column3:
        return board[2]
    return
def checkDiagonalWin():
    global gameStillGoing
    diagonal1 = board[0] == board[4] == board[8] != '-'
    diagonal2 = board[2] == board[4] == board[6] != '-'
    if diagonal1 or diagonal2:
        gameStillGoing = False
    if diagonal1:
        return board[0]
    if diagonal2:
        return board[2]
    return
#checkTie - In case there's no form of sequence, then there is a tie(i.e no one of the player won)
def checkTie():
    global gameStillGoing
    if '-' not in board:
        gameStillGoing = False
    return
#flipPlayer - alternates the players to play next (the function uses the the current player stats)
def flipPlayer():
    global player
    #specifiyCurrentPlayer
    if player == 'X' or player == 'x':
        print('Current player is '+player)
    elif player == 'O' or player == 'o':
        print('Current player is '+player)
    #specifyNextPlayer
    if player == 'X' or player == 'x':
        print('The next player is O')
    elif player == 'O' or player =='o':
        print('The next player is X')   
    #selectNextPlayer
    if player == 'X' or player == 'x':
        player = 'O' or 'o'
    elif player == 'O' or player =='o':
        player = 'x' or 'X'   
    

playGame()