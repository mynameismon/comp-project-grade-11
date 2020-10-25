#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 19:50:15 2020

@author: bezbakri

python help
"""
"""
_____________________________________________
|Problem : Given a tuple pairs = {(2,5),    |
|(4,2),(9,8),(12,10)}, count the number of  |
|pairs  (a,b) such that both a and b are    |
|even                                       |
|-------------------------------------------|
| Approach:                                 |
| We use a for loop to iterate through all  |
| of the pairs. We then use the modulo      |
| operator to check if both items in a pair |
| are even or not. We then store the number |
| of even pairs in a variable and print it  |
|-------------------------------------------|
"""
#Solution :-

tuple_pairs = {(2,5),(4,2),(9,8),(12,10)} #set of tuple pairs

count_even_pairs = 0 #variable to store the number of tuples with both elements being even


for i in tuple_pairs:
    if i[0] %2 == 0 and i[1] % 2 == 0:
        count_even_pairs += 1
      
print("Number of tuples with both elements being even are ", count_even_pairs)