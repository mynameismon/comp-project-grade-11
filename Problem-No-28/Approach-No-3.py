#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 16:51:43 2020

@author: bezbakri
"""


'''
| print pattern:                           |
| 54321                                    |
| 5432                                     |
| 543                                      |
| 54                                       |
| 5                                        |
|------------------------------------------|
| nested for-loops used for the numbering  |
'''



for i in range(5):
    res = ""       #emptying res so that the previous pattern is erased
    for j in range(5,i,-1):
        res+=str(j)
    print(res)