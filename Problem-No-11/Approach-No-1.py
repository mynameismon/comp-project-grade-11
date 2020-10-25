'''
| Write a program to generate the Fibonacci series till first ‘n’ numbers                     |
|---------------------------------------------------------------------------------------------|
| We use the input() function to receive input from the user and print() function to print it |
'''

n = int(input("Enter number \n"))
a = 0
b = 1
while a<n:
    a,b = b,a+b
    print(a)
