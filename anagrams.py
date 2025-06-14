'''
PCAP PE2 Module 2 
LAB

Estimated time
30-60 minutes

Level of difficulty
Easy

Objectives
improving the student's skills in operating with strings;
converting strings into lists, and vice versa.
Scenario
An anagram is a new word formed by rearranging the letters of a word, using all the original letters exactly once. For example, the phrases "rail safety" and "fairy tales" are anagrams, while "I am" and "You are" are not.

Your task is to write a program which:

asks the user for two separate texts;
checks whether, the entered texts are anagrams and prints the result.
Note:

assume that two empty strings are not anagrams;
treat upper- and lower-case letters as equal;
spaces are not taken into account during the check - treat them as non-existent
Test your code using the data we've provided.

Test data
Sample input:

Listen
Silent

Sample output:

Anagrams


Sample input:

modern
norman

Sample output:

Not anagrams

'''

var_1 = input('Enter your first word :')
var_2 = input('Enter your second word :')

var_1_list = list(var_1.replace(" ", "").lower())
var_2_list = list(var_2.replace(" ", "").lower())

all_var = True


for letter in var_1_list:
    if letter in var_2_list:
        var_2_list.remove(letter)
    else:
        all_var = False

if all_var and len(var_2_list) == 0:
    print("Anagrams")
else:
    print("Not Anagrams")