'''
| Write a program to check whether a number is an Armstrong number                            |
|---------------------------------------------------------------------------------------------|
| We use the input() function to receive input from the user and print() function to print it |
'''

n = str(input("Enter the number \n"))

res = []
x = len(n)

res = [int(i)**x for i in n]
print(sum(res)==int(n))
