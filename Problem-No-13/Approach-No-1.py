'''
| Write a program to check if the given string is a palindrome or not                         |
|---------------------------------------------------------------------------------------------|
| We use the input() function to receive input from the user and print() function to print it |
'''

n = str(input("Enter word \n"))

x = len(n)//2
res = True
if len(n)>1:
    for i in range(x):

        if n[i] != n[len(n)-i -1]:
            res = False
            break
print(f'Is {n} a palindrome? {res}')