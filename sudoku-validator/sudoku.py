'''
PCAP PE2 Module 2 

LAB
Estimated time
60-90 minutes

Level of difficulty
Hard

Objectives
improving the student's skills in operating with strings and lists;
converting strings into lists.
Scenario
As you probably know, Sudoku is a number-placing puzzle played on a 9x9 board. The player has to fill the board in a very specific way:

each row of the board must contain all digits from 0 to 9 (the order doesn't matter)
each column of the board must contain all digits from 0 to 9 (again, the order doesn't matter)
each of the nine 3x3 "tiles" (we will name them "sub-squares") of the table must contain all digits from 0 to 9.
If you need more details, you can find them here.

Your task is to write a program which:

reads 9 rows of the Sudoku, each containing 9 digits (check carefully if the data entered are valid)
outputs Yes if the Sudoku is valid, and No otherwise.
Test your code using the data we've provided.

Test data
Sample input:

295743861
431865927
876192543
387459216
612387495
549216738
763524189
928671354
154938672

Sample output:

Yes


Sample input:

195743862
431865927
876192543
387459216
612387495
549216738
763524189
928671354
254938671

Sample output:

No
'''
import time

sample_solve1 = [
    [2,9,5,7,4,3,8,6,1],
    [4,3,1,8,6,5,9,2,7],
    [8,7,6,1,9,2,5,4,3],
    [3,8,7,4,5,9,2,1,6],
    [6,1,2,3,8,7,4,9,5],
    [5,4,9,2,1,6,7,3,8],
    [7,6,3,5,2,4,1,8,9],
    [9,2,8,6,7,1,3,5,4],
    [1,5,4,9,3,8,6,7,2]
]
sample_solve2 = [
    [1,9,5,7,4,3,8,6,2],
    [4,3,1,8,6,5,9,2,7],
    [8,7,6,1,9,2,5,4,3],
    [3,8,7,4,5,9,2,1,6],
    [6,1,2,3,8,7,4,9,5],
    [5,4,9,2,1,6,7,3,8],
    [7,6,3,5,2,4,1,8,9],
    [9,2,8,6,7,1,3,5,4],
    [2,5,4,9,3,8,6,7,9]
]

def is_all_horizontal(list):
    for row in list:
        sum = 0
        for i in row:
            sum += i
        if sum != 45:
            return False
    return True


def is_all_vertical(list):

    j = 0

    while j < 9:
        sum = 0
        for i in range(len(list)):
            sum += list[i][j]
        
        j += 1
              
        if sum != 45:
            return False
    return True


def is_all_square(list):

    a = 0
    while a < 9:
        b = 0
        while b < 9:
            sum = 0
            for x in range(a , a+3):
                for y in range(b , b+3):
                    sum += list[x][y]

            if sum != 45:
                return False
            
            b += 3
        a += 3

        
    return True


def is_sudoku(list):
    all_horizontal = is_all_horizontal(list)
    all_vertical = is_all_vertical(list)
    all_square = is_all_square(list)

    if all_horizontal and all_vertical and all_square:
        print("Victory! Sudoku conquered.")
    else:
        print("This puzzle’s still playing hard to get. Give it another shot!!!")


def play_sudoku():
    playing = False

    while not playing:

        player_input = input("To play Sudoku enter 9 rows of 9 integer ranging from 1 to 9 ( left-to-right & top-to-bottom) :")
        valid_input = ''
        for num in player_input:
            if num.isdigit():
                valid_input += num
        
        if len(valid_input) == 81:
            playing = True
            return valid_input

        else:
            print( " That is the incorrect amount of integers it should be 81 try again!")

def playing_sudoku(solution):


    board = []
    for i in range(len(solution)):
        if i % 9 == 0:
            row = []
            row.append(int(solution[i]))
        elif (i + 1) % 8 == 0:
            row.append(int(solution[i]))
            board.append(row)
        else:
            row.append(int(solution[i]))


    print('Putting the pieces together...Sudoku mastery in progress!')
    time.sleep(4)

    is_sudoku(board)

        





user_solution = play_sudoku()
playing_sudoku(user_solution)
# print(is_sudoku(sample_solve2))