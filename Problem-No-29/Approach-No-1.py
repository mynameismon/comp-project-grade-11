"""
Created on Mon Oct 26 16:42:04 2020

@author: bezbakri
"""
"""
_____________________________________________
| Problem : Write a program to create a     |
| nested tuple to store marks of three      |
| subjects for five students. Compute the   |
| total marks and average obtained by each  |
| student                                   |
|-------------------------------------------|
| Approach:                                 |
| First, we make a sample nested tuple.     |
| Nest, we use a for loop to read all the   |
| the nested tuples. We then use another for|
| loop to find the total marks for each     |
| student by adding each element of the     |
| tuple. The average of a student is found  |
| by dividing the total merks by number of  |
| subjects/ elements in a nested tuple (3)  |
|-------------------------------------------|
"""


nested_tuple = ((30, 40, 50), (72, 68, 76), (63, 69, 57),\
                (60, 57, 80), (65, 67, 68))
stud_num = 1
for i in nested_tuple:
    print(f"for student {stud_num}")
    marks_total = 0
    marks_avg = 0
    for j in i:
        marks_total+=j
    marks_avg = marks_total/3
    print(f"Total marks obtained is {marks_total}")
    print(f"Average marks obtained is {marks_avg}")    
    stud_num+=1
