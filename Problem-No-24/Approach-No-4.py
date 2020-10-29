#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 20:28:19 2020

@author: bezbakri
"""

'''
| 1+ x^2 + x^3 + x^4 + x^5 +... + x^n                                                        |
|--------------------------------------------------------------------------------------------|
| Usage of the formula                                                                       |
'''

x = int(input("Enter x: "))
n = int(input("Enter n: "))
res = 1

for i in range (2,n+1):
    res+=x**i
     
print(f"Sum of {n} terms is {res}")