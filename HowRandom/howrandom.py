# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 10:31:05 2018

@author: Wey Yi
"""

import random
import matplotlib.pyplot as plt

d = 100

x = []
y = []

for i in range(d):
    x.append(random.random())
    y.append(i)
    
plt.scatter(x,y,s=1)