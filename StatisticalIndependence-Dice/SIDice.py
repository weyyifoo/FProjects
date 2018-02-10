# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 14:33:58 2018

@author: Wey Yi
"""

import random
import matplotlib.pyplot as plt
import numpy as np

result = []

d = 10000000
for i in range(d):
    result.append(random.randint(1, 6))

k = []

for m in range(1,7):
    for n in range(1, 7):
        count = 0
        for p in range(0, d-1):    
            if result[p] == m and result[p + 1] == n:
                count += 1
        k.append((count/(d-1))*100)

# count the number of occurences for possibilities 1 through 6
countocc = []
for a in range(1,7):
    q = result.count(a)
    countocc.append(q)

# Yield successive n-sized chunks from list 'l'
def chunks(l, n):
     
    # looping till length l
    for i in range(0, len(l), n): 
        yield l[i:i + n]
 
# How many elements each
# list should have
n = 6
 
x = list(chunks(k, n))
x_array = np.asarray(x)