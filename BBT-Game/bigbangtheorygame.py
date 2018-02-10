# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 19:11:39 2018

@author: Wey Yi
"""

# a simple rock vs scissors vs paper vs lizard vs spock game inspired by The Big Bang Theory
# user inputs choice
# computer inputs by randint module

from random import randint

print("Here are the rules:")
print("Scissors cuts Paper")
print("Paper covers Rock")
print("Rock crushes Lizard")
print("Lizard poisons Spock")
print("Spock smashes Scissors")
print("Scissors decapitates Lizard")
print("Lizard eats Paper")
print("Paper disproves Spock")
print("Spock vaporizes Rock")
print("(and as it always has) Rock crushes scissors")

user = input("rock (r), paper (p), scissors (s), lizard (l), spock (k)?")


chosen = randint(1,5)

if chosen == 1:
    computer = 'r'
elif chosen == 2:
    computer = 'p'
elif chosen == 3:
    computer = 's'
elif chosen == 4:
    computer = 'l'
else:
    computer = 'k'
    

print(user,"vs", computer)

if user == computer:
    print("its a draw!")
elif user == 'r' and computer == 'p':
    print ('Paper covers Rock - Computer wins!')
elif user == 'p' and computer == 'r':
    print ('Paper covers Rock - You win!')
elif user == 'p' and computer == 's':
    print ('Scissors cuts Paper - Computer wins!')
elif user == 's' and computer == 'p':
    print ('Scissors cuts Paper - You win!')
elif user == 's' and computer == 'r':
    print ('Rock crushes scissors - Computer wins!')
elif user == 'r' and computer == 's':
    print ('Rock crushes scissors - You win!')
elif user == 'l' and computer == 'r':
    print ('Rock crushes Lizard - Computer wins!')
elif user == 'r' and computer == 'l':
    print ('Rock crushes Lizard - You win!')
elif user == 's' and computer == 'k':
    print ('Spock smashes Scissors - Computer wins!')
elif user == 'k' and computer == 's':
    print ('Spock smashes Scissors - You win!')
elif user == 'k' and computer == 'p':
    print ('Paper disproves Spock - Computer wins!')
elif user == 'p' and computer == 'k':
    print ('Paper disproves Spock - You win!')
elif user == 'p' and computer == 'l':
    print ('Lizard eats Paper - Computer wins!')
elif user == 'l' and computer == 'p':
    print ('Lizard eats Paper - You win!')
elif user == 'r' and computer == 'k':
    print ('Spock vaporizes Rock - Computer wins!')
elif user == 'k' and computer == 'r':
    print ('Spock vaporizes Rock - You win!')
elif user == 'l' and computer == 's':
    print ('Scissors decapitates Lizard - Computer wins!')
elif user == 's' and computer == 'l':
    print ('Scissors decapitates Lizard - You win!')
elif user == 'k' and computer == 'l':
    print ('Lizard poisons Spock - Computer wins!')
elif user == 'l' and computer == 'k':
    print ('Lizard poisons Spock - You win!')