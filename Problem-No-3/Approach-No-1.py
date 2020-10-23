"""
|-------------------------------------------|
| Problem 3:⦁   Write a program to find the |
| largest of three numbers                  |
|-------------------------------------------|
| Approach:                                 |
| We use the input() function to receive    |
| input from the user and the print()       |
| function to print it.                     |
|-------------------------------------------|
"""

a = int(input("Number 1: \n"))
b = int(input("Number 2: \n"))
c = int(input("Number 3: \n"))

res = max([a,b,c])
print(f"The highest is {res}")


