'''
| Ask the user to enter a list of strings. Create a new list that contains only those strings which start with a vowel |
|----------------------------------------------------------------------------------------------------------------------|
| Using split(), for-loops and if-statements                                                                           |
'''

n = input("Input a list of strings seperated by commas[,]\n")
res = ''
n = n.split(',')
vowels = 'AEIOUaeiou'

for i in n:
    if i[0] in vowels:
        res += i
print(res)


