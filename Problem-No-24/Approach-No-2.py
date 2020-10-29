#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 19:49:33 2020

@author: bezbakri
"""


'''
| 1^2+2^2+3^2... + n^2                                                                               |
|--------------------------------------------------------------------------------------------|
| Usage of the formula                                                                       |
'''

n = int(input("Enter last term\n"))

print(f'The sum of the series is {n*(n+1)*(2*n+1)/6}')