#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 20:00:24 2020

@author: bezbakri
"""

'''
|----------------------------------------------|
|x - x^2/2! + x^3/3! - x^4/4! + x^5/5! - x^6/6!|
|----------------------------------------------|
| use of nested for loops                      |
|----------------------------------------------|
'''

x = int(input("Enter x: "))
res = x
sign = -1
for i in range (2,7):
    f = 1
    for j in range (1, i+1):
        f*=j
    term = (sign*(x**i))/f
    res += term
    sign*=-1
print(f"Sum of terms is {res}")