'''
| Ask the user to enter a list of strings. Create a new list that contains only those strings which start with a vowel |
|----------------------------------------------------------------------------------------------------------------------|
| Using split(), for-loops and if-statements                                                                           |
'''

n = []
while True:
    n_in = input("Enter some string. To exit, type exit0: ")
    if n_in == "exit0":
        break
    else:
        n.append(n_in)

vowels = 'AEIOUaeiou'

res = []

for i in n:
    if i[0] in vowels:
        res.append(i)
print(res)
