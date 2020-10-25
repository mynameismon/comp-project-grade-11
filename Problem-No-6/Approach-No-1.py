'''
| Write a program to find the factorial of a number.                                          |
|---------------------------------------------------------------------------------------------|
| We use the input() function to receive input from the user and print() function to print it |
'''

num = int(input("Enter number: \n"))
x = 1
if(x>=1):
    for i in range(num,1,-1):
        x *= i
    print(x)
else:
    print("Can't use negative numbers...")

