# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 11:49:59 2021

@author: victor jimenez
"""

# Spring 2021
# Homework 1

# Victor Jimenez
# victorjimenez15

# Due date: Sunday April 11th before midnight
# Write your answers in the space between the questions, and commit/push only this file to your repo.
# Note that there can be a difference between giving a "minimally" right answer, and a really good
# answer, so it can pay to put thought into your work.

#############

# Question 1: Using a for loop, write code that takes in any list of objects, then prints out:
# "The value at position __ is __" for every element in the loop, where the first blank is the
# index location and the second blank the object at that index location.
list_1 = ['a','e','i','o','u']
for letter in list_1:
    index = list_1.index(letter)
    print('The value at position', index, 'is', letter )
#cite: https://www.tutorialspoint.com/accessing-index-and-value-in-a-python-list

# Question 2: A palindrome is a word or phrase that is the same both forwards and backwards. Write
# code that takes a variable of any string, then tests to see whether it qualifies as a palindrome.
# Make sure it counts the word "radar" and the phrase "A man, a plan, a canal, Panama!", while
# rejecting the word "Apple" and the phrase "This isn't a palindrome". Print the results.
string_1 = 'radar'
string_2 = 'A man, a plan, a canal, Panama!'
string_3 = 'Apple'
string_4 = 'This isnt a palindrome'
list_2 = [string_1, string_2, string_3, string_4]

punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~' ''' 
list = [''.join(c for c in s if c not in punctuation) for s in list_2]
mapped = [str.lower() for str in list]

for string in mapped:
    if string == string[::-1]:
        print("The string is a palindrom")
    else:
        print("The string is not a palindrome.")  
#cite: https://stackoverflow.com/questions/31633635/what-is-the-meaning-of-inta-1-in-python
#cite: https://gist.github.com/mcescalante/7921270
        
        
# Question 3: The code below pauses to wait for user input, before assigning the user input to the
# variable.  Beginning with the given code, check to see if the answer given is an available
# vegetable.  If it is, print that the user can have the vegetable and end the bit of code.  If
# they input something unrecognized by our list, tell the user they made an invalid choice and make
# them pick again.  Repeat until they pick a valid vegetable.
available_vegetables = ['carrot', 'kale', 'radish', 'pepper']
choice= input('Please pick a vegetable I have available:')

while choice not in available_vegetables: 
      choice=input('Invalid choice, please pick again an available vegetalble:')
      continue
if choice in available_vegetables:
    print('The user can have the vegetable') 

    
# Question 4: Write a list comprehension that starts with any list of strings, and returns a new
# list that contains each string in all lower-case letters, but only if the string begins with the
# letter "a" or "b".

string_41 = 'SUPERMAN'
string_42 = 'AQUAMAN'
string_43 = 'BATMAN'
string_44 = 'WONDER WOMAN'
Justice_League = [string_41, string_42, string_43, string_44]

mapped = [str.lower() for str in Justice_League if (str.startswith('A') or (str.startswith('B')))]
print (mapped)


# Question 5: Beginning with the list below, write a single list comprehension that turns it into
# the following list: [26, 22, 18, 14, 10, 6]
start_list = [3, 5, 7, 9, 11, 13]

new_list = [element * 2 for element in start_list]
new_list.reverse()
print(new_list)
#cite: https://www.kite.com/python/answers/how-to-multiply-each-element-of-a-list-by-a-number-in-python

# Question 6: Beginning with the two lists below, write a single dictionary comprehension that
# turns them into the following dictionary: {'IL':'Illinois', 'IN':'Indiana', 'MI':'Michigan', 'OH':'Ohio'}
short_names = ['IL', 'IN', 'MI', 'OH']
long_names  = ['Illinois', 'Indiana', 'Michigan', 'Ohio']

res = {short_names[i]: long_names[i] for i in range(len(short_names))}
print ("Diccionary is: " +  str(res))
#cite:https://www.w3schools.com/python/ref_func_len.asp