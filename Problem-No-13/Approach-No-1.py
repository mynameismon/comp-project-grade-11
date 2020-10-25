'''
| Write a program to check if the given string is a palindrome or not                         |
|---------------------------------------------------------------------------------------------|
| for-loop from both sides of the string                                                      |
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