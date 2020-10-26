#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 15:46:21 2020

@author: bezbakri
"""

"""
|-------------------------------------------|
| Problem 6: Write a program to find the    |
| factorial of a number                     |
|-------------------------------------------|
| Approach:                                 |
| First, we take in a number using the      |
| input() function. Then, we check if the   |
| number is a positive integer or not. Is it|
| is, then we use a for loop to keep        |
| multiplying all integers upto that number |
|-------------------------------------------|
"""

num = int(input("Enter a number: "))
factorial_num = 1

if num == 0:
    print(f"Factorial is {factorial_num}")
elif num < 0:
    print("No factorials for negative numbers")
else:
    for i in range (1, num+1):
        factorial_num *=i
    print(f"Factorial is {factorial_num}")