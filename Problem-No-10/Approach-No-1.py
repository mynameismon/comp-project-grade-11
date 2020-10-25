'''
| Write a program to perform all the mathematical operations on a set of values.              |
|---------------------------------------------------------------------------------------------|
| We use the input() function to receive input from the user and print() function to print it |
'''

num1 = int(input("Enter first number\n"))
num2 = int(input("Enter second number\n"))

op = str(input("Enter operation\n"))

if op=='/' or op=='divide':
    print(num1/num2)
elif op=='*' or op=='multiply':
    print(num1*num2)
elif op=='+' or op=='add':
    print(num1*num2)
elif op=='-' or op=='subtract':
    print(num1-num2)
