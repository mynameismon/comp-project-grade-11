'''
| Write a program to find the area of a triangle using Heroin’s formula                       |
|---------------------------------------------------------------------------------------------|
| Using the math module                                                                       |
'''
import math
a = int(input("Side a: \n"))
b = int(input("Side b: \n"))
c = int(input("Side c: \n"))
s = (a+b+c)/2
area = math.sqrt(s*(s-a)*(s-b)*(s-c))
print(f"Area of triangle is {area}")


