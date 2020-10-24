'''
| Write a program to find if a given number is prime or not.                                  |
|---------------------------------------------------------------------------------------------|
| We use the input() function to receive input from the user and print() function to print it |
'''

num = int(input("Enter the number :\n"))
res = True
for i in range(2,num):
    if num%i == 0:
        res = False
print(res)