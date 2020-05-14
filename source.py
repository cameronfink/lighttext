# This is a word processor designed to word process
import random
from random import randrange, seed, random, randint
from os import system, name 
from time import sleep 

# Clear function
def clear(): 
  
    # Windows function
    if name == 'nt': 
        _ = system('cls') 
  
    # Other OS function
    else: 
        _ = system('clear') 
  
# Copyright and welcome
print('Welcome to LightText v0.1') 
print('This program is designed to be light and easy to run.')
print('The program will walk you through all steps.')
print('Please remember to use enter only when you are ready to submit.')
print('\n') 
print('Copyright Cameron Fink 2020')

# Clear screen
sleep(5) 
clear() 

# Title the document
title = str(input('Title your document: '))

# Open text file to write
file = open(title + '.txt', 'w')

# Author the document
author = str(input('Name the author of the document: '))

# Write the body of the document
body = str(input('Only use enter when you are ready to complete. Write the body of your document: '))

# Write the inputs to the file
file.write(title)
file.write('\n')
file.write(author)
file.write('\n')
file.write('\n')
file.write(body)

# Success message
print('\n')
print('Your document has been saved as' + title + '.txt')

# Clear screen
sleep(3)
clear()
