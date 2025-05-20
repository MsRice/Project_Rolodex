# Python Institute - lab : Tic-Tac-Toe

# Write a simple program which pretends to play tic-tac-toe with the user. To make it all easier for you, we've decided to simplify the game. Here are our assumptions:

# the computer (i.e., your program) should play the game using 'X's;
# the user (e.g., you) should play the game using 'O's;
# the first move belongs to the computer − it always puts its first 'X' in the middle of the board;
# all the squares are numbered row by row starting with 1 see the example session below for reference)
# the user inputs their move by entering the number of the square they choose − the number must be valid, i.e., it must be an integer, it must be greater than 0 and less than 10, and it cannot point to a field which is already occupied;
# the program checks if the game is over − there are four possible verdicts: the game should continue, the game ends with a tie, you win, or the computer wins;
# the computer responds with its move and the check is repeated;
# don't implement any form of artificial intelligence − a random field choice made by the computer is good enough for the game.
import time
import random


def clear_board():
    return [[1,2,3] , [4,5,6] , [7,8,9]]

def display_board(board ,player):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.

    print(F'Player {player}\'s Turn !')
    for row in board:
        print((('+'+'-'*16)*3) + '+' )
        print((('|'+' '*16)*3) + '|' )


        for i in row:
            print(f'|        {i}       ', end="")
            #Bonus: figure out how to do string multiplication in f' interpolaization

        print('|'+"\n"+(('|'+' '*16)*3) + '|' )


    print((('+'+'-'*16)*3) + '+' )

def switch_player(player):
    if player == "X":
        return "O"
    return "X"

def get_random_except(excluded):
           
    num = random.randint(1, 8)
    
    if num in excluded:
        if len(excluded) == 9:
            draw()
        return get_random_except(excluded)
    else:
        excluded.append(num)
        return num , excluded

def draw():
    print((('+'+'-'*16)*3) + '+' )
    print(('|'+' '*50) + '|' )
    print(('|'+' '*50) + '|' )
    print(('|'+' '*10) + "This game is a draw!" + (' '*20 +'|'))
    print(('|'+' '*50) + '|' )
    print(('|'+' '*50) + '|' )
    print(('|'+' '*10) + "Would you like to play again?" + (' '*11 +'|') +" \n"  + ('|'+' '*15) +  "1. Yes"+ (' '*29 +'|') +"\n"+('|'+' '*15) + "2. No" + (' '*30 +'|'))
    print(('|'+' '*50) + '|' )
    print(('|'+' '*50) + '|' )
    print((('+'+'-'*16)*3) + '+' )
    
    ans = int(input())
    global excluded

    if ans == 1:
        board = clear_board()
        excluded = []
        
        game_play(board , winner=False , player="X" )  

    else:
        print("Thanks for playing!")
        exit()


def winner(player):
        print((('+'+'-'*16)*3) + '+' )

        print(('|'+' '*50) + '|' )
        print(('|'+' '*50) + '|' )
        print(('|'+' '*10) + "Player " + player + " has won!" + (' '*23 +'|'))
        print(('|'+' '*50) + '|' )
        print(('|'+' '*50) + '|' )
        print(('|'+' '*10) + "Would you like to play again?" + (' '*11 +'|') +" \n"  + ('|'+' '*15) +  "1. Yes"+ (' '*29 +'|') +"\n"+('|'+' '*15) + "2. No" + (' '*30 +'|'))
        print(('|'+' '*50) + '|' )
        print(('|'+' '*50) + '|' )
        print((('+'+'-'*16)*3) + '+' )
        ans = int(input("? : "))
        global excluded

        if ans == 1:
            board = clear_board()
            excluded = []
            
            game_play(board , winner=False , player="X" )  

        else:
            print("Thanks for playing!")
            exit()


def is_winner(player , board):

    if row_winner(player ,board):
        return winner(player)
    if column_winner(player ,board):
        return winner(player)
    if diagonal_winner(player ,board):
        return winner(player)

    return False

def row_winner(player ,board):
    checked = True
    for row in board:
       checked = True if row.count(player) == 3 else False
       if checked == True:
           return True
    return checked

def column_winner(player ,board):
    for i in range(3):
        count = 0
        for row in board:
            count = count+1 if row[i] == player else count
            if count == 3:
                return True
    return False

def diagonal_winner(player ,board):
    count = 0

    if board[0][0] == player:
        i = 0
        for row in board:
            count = count+1 if row[i] == player else count
            i += 1
            if count == 3:
                return True
    elif board[0][2] == player:
        i = 2
        for row in board:
            count = count+1 if row[i] == player else count
            i -= 1
            if count == 3:
                return True
        
    return False

def enter_move(board  , player , excluded):
    # The function accepts the board's current status
    # checks the input, and updates the board according to the user's decision.
    is_valid = False
    
    
    while is_valid == False:
        try:
            move = int(input("Enter the Space number you would like to place your X : "))
            if move > 0  and move < 10: 
                # Check board space is empty
                a = (move-1) // 3
                b = (move  - (a* 3)) - 1

                if type(board[a][b]) == int:
                    board[a][b] = player

                    winner = is_winner(player , board) 
                    player = switch_player(player)
                    excluded.append(move)
                    return board , winner , player
                else:
                    print(f'{move} is an invalid move! Choose an open space')
                    continue

            else:
                print("Entry is Unavailable Must be between 1-9")
        except ValueError:
            print("Input must be a integer!")
       
def enter_comp_move(board  , player , excluded):
    # The function accepts the board's current status
    # checks the input, and updates the board according to the user's decision.
    is_valid = False

    while is_valid == False:
            move , excluded = get_random_except(excluded)

            # Check board space is empty
            a = (move-1) // 3
            b = (move  - (a* 3)) - 1
            if type(board[a][b]) == int:
                board[a][b] = player

                winner = is_winner(player , board) 
                player = switch_player(player)
                return board , winner , player
            
    
          
        
       


    return(None ,None ,None)
       
def game_play(board , winner , player ):
    display_board(board , player)
    while winner == False:
        if player == "X":
            board , winner , player = enter_move(board , player, excluded)
            print("winner here" , winner)
            display_board(board , player)
        
        if player == "O":
            print("Player is thinking ...")
            time.sleep(1)
            board , winner , player = enter_comp_move(board , player ,excluded)
            display_board(board , player)

            
            print("polin_bridgerton has played with my heart")
            winner = False
            


board = clear_board()

excluded = []

game_play(board , winner=False , player="X" )  