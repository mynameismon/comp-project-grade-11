'''
| Write a program to find the roots of the quadratic equation                                 |
|---------------------------------------------------------------------------------------------|
| Using quadratic equation fromula                                                            |
'''
from math import sqrt
a = int(input("Enter coefficient of x^2 : \n"))
b = int(input("Enter coefficient of x : \n"))
c = int(input("Enter constant : \n"))

root1 = (-b + sqrt(b**2 -4*a*c))/(2*a)
root2 = (-b - sqrt(b**2 -4*a*c))/(2*a)

print(f"Roots are {root1} and {root2}")



