'''
LAB

Estimated time
30 minutes

Level of difficulty
Medium

Objectives
improving the student's skills in operating with strings;
using strings to represent non-text data.
Scenario
You've surely seen a seven-segment display.

It's a device (sometimes electronic, sometimes mechanical) designed to present one decimal digit using a subset of seven segments. If you still don't know what it is, refer to the following Wikipedia article.

Your task is to write a program which is able to simulate the work of a seven-display device, although you're going to use single LEDs instead of segments.

Each digit is constructed from 13 LEDs (some lit, some dark, of course) - that's how we imagine it:

  # ### ### # # ### ### ### ### ### ### 
  #   #   # # # #   #     # # # # # # # 
  # ### ### ### ### ###   # ### ### # # 
  # #     #   #   # # #   # # #   # # # 
  # ### ###   # ### ###   # ### ### ###

Note: the number 8 shows all the LED lights on.

Your code has to display any non-negative integer number entered by the user.

Tip: using a list containing patterns of all ten digits may be very helpful.

Test data
Sample input:

123

Sample output:

  # ### ### 
  #   #   # 
  # ### ### 
  # #     # 
  # ### ### 

Sample input:
9081726354

Sample output:

### ### ###   # ### ### ### ### ### # # 
# # # # # #   #   #   # #     # #   # # 
### # # ###   #   # ### ### ### ### ### 
  # # # # #   #   # #   # #   #   #   # 
### ### ###   #   # ### ### ### ###   # 


'''


led_numbers = {
    "0" : [True, True, True, False, True, True, True],
    "1" : [False, False, True, False, False, True, False],
    "2" : [True, False, True, True, True, False, True],
    "3" : [True, False, True, True, False, True, True],
    "4" : [False, True, True, True, False, True, False],
    "5" : [True, True, False, True, False, True, True],
    "6" : [False, True, False, True, True, True, True],

    "7" : [True, False, True, False, False, True, False],
    "8" : [True, True, True, True, True, True, True],
    "9" : [True, True, True, True, False, True, False]
}

def display_led(lst):
    top = ''
    toplayer = ''
    middle = ''
    lowlayer = ''
    bottom = ''

    horizontal_0 = "        "
    horizontal_1 = "#####   "
    vert_01 = "    #   "
    vert_10 = "#       "
    vert_00 = "        "
    vert_11 = "#   #   "

    for num in lst:
        ## Top ##
        if led_numbers[num][0]:
            top += horizontal_1
        elif not led_numbers[num][0]:
            top += horizontal_0

        ## Middle ##

        if led_numbers[num][3]:
            middle += horizontal_1
        elif not led_numbers[num][3]:
            middle += horizontal_0

        ## Bottom ##

        if led_numbers[num][6]:
            bottom += horizontal_1
        elif not led_numbers[num][6]:
            bottom += horizontal_0

        ## Top vertical Layer
        
        if led_numbers[num][1] and led_numbers[num][2]:
            toplayer += vert_11
        elif led_numbers[num][1] and not led_numbers[num][2]:
            toplayer += vert_10
            
        elif not led_numbers[num][1] and led_numbers[num][2]:
            toplayer += vert_01
        elif not led_numbers[num][1] and not led_numbers[num][2]:
            toplayer += vert_00
            print(led_numbers[num][1] , led_numbers[num][2] )

        ## Lower vertical Layer

        if led_numbers[num][4] and led_numbers[num][5]:
            lowlayer += vert_11
        elif led_numbers[num][4] and not led_numbers[num][5]:
            lowlayer += vert_10
            
        elif not led_numbers[num][4] and led_numbers[num][5]:
            lowlayer += vert_01
        elif not led_numbers[num][4] and not led_numbers[num][5]:
            lowlayer += vert_00



    print(top)
    print(((toplayer + '\n')* 3).rstrip())
    print(middle)
    print(((lowlayer + '\n')* 3).rstrip())
    print(bottom)


def display_number(number):
    if type(number) is int :
        number = list(str(number))
        
    display_led(number)

display_number(14)


