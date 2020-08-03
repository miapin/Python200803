# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 15:25:23 2020

@author: AE401
"""

M=input("please enter your math score:")
M=int(M)
E=input("please enter your english score:")
E=int(E)
if M>=90 and E>=90:
    print("Great job!")
elif M<=60 and E<=60:
    print("You need to stay at school until 9.")
else:
    print("Keep going!")