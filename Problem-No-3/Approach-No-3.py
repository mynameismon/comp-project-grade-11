"""
|-------------------------------------------|
| Problem 3:⦁   Write a program to find the |
| largest of three numbers                  |
|-------------------------------------------|
| Approach:                                 |
|         We use the max() function         |
|-------------------------------------------|
"""

a = int(input("Number 1: \n"))
b = int(input("Number 2: \n"))
c = int(input("Number 3: \n"))

nums = [a, b, c]
nums.sort()
print("The largest number is:", nums[-1])