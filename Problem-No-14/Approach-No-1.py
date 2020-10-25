'''
| Write a program to input 3 sides of a triangle and prints whether it is an equilateral, isosceles or scale triangle |
|---------------------------------------------------------------------------------------------------------------------|
| We use the input() function to receive input from the user and print() function to print it                         |
'''

n = input("Enter sides, seperated by commas[,] \n")
n = [int(i) for i in n.split(',')]

a,b,c = n

if a==b and b==c and c==a:
    print("Equilateral")
elif a!=b and b!=c and c!=a:
    print("Scalene")
else:
    print("Isoceles")