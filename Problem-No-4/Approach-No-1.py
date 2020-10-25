"""
|-------------------------------------------|
| Problem 4: Write a program to find whether|
| the year is a leap year or not.           |
|-------------------------------------------|
| Approach:                                 |
| We use the input() function to receive    |
| input from the user and the print()       |
| function to print it.                     |
|-------------------------------------------|
"""


year = int(input("Enter year: "))

print("Is the year leap?")
print(year%4==0)

