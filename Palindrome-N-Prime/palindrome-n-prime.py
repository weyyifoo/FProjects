# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 10:29:26 2018

@author: Wey Yi
"""

# code checks to see if the number is a prime number
def isPrime(s):
    s = int(s)
    d = 0
    for n in range(3,s):
        if s % n == 0: # if there is a remainder from dividing s by the counter, n, then the code adds 1 to d
            d += 1
        else:
            d += 0
    if d == 0: # if d does not clock up any number at the end of the run, it is a prime number
        return True
    else:
        return False

# code checks to see if the input is a palindrome:
def isPalin(s):
    rev = s[::-1]
    if s == rev:
        return True
    else:
        return False

s = str(input("Input number to test if Palindrome & Prime: "))
a = isPalin(s)
k = isPrime(s)

if a == 1 and k == 1:
    print("Yes. The input is both a Prime Number and a Palindrome")
elif (a == 1) and (k == 0):
    print("The input is only a Palindrome. It is not a Prime")
elif (a == 0) and (k == 1):
    print("The input is only a Prime. It is not a Palindrome")
else:
    print("The input is neither a Prime nor Palindrome")