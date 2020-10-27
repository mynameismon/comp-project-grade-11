"""
|-------------------------------------------|
| Problem 4: Write a program to find whether|
| the year is a leap year or not.           |
|-------------------------------------------|
| Approach:                                 |
| First, check if the year is divisible by  |
| 100. If so, check is the year is          |
| divisible by 400. If not, simple division |
| by 4 is done                              |
|-------------------------------------------|
"""


year = int(input("Enter year: "))

print("Is the year leap?")
if year%100 == 0:
    print(year%400 == 0)
else:
    print(year%4 == 0)

