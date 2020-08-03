# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 14:56:41 2020

@author: AE401
"""

height1=input("please enter your height:")
height1=int(height1)
height=height1/100
weight=input("please enter your weight:")
weight=int(weight)
BMI=weight//height**2
if BMI<18.5:
    print("體重不足")
elif BMI<24:
    print("正常")
elif BMI<27:
    print("過重")
elif BMI<30:
    print("輕度肥胖")
elif BMI<35:
    print("中度肥胖")
else:
    print("重度肥胖")
    