'''
| Write a program to generate the Fibonacci series till first ‘n’ numbers                     |
|---------------------------------------------------------------------------------------------|
| Usage of for-loops                                                                        |
'''

n = int(input("Enter number \n"))
a = 0
b = 1
for i in range(n):
    a,b = b,a+b
    print(a)
