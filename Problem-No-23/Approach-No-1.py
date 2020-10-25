'''
| Write a program that should prompt the user to type some sentences. It should then print number of words, number of characters, number of digits and number of special characters in it. |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| We use the input() function to receive input from the user and print() function to print it                                                                                              |
'''

string = input("Enter a sentence...\n")
numbers = '1234567890'
chars = '!@#$%^&*()<>?:-\"\'}+=_{|\][;//.,`~'
num_words = len(string.split())
res = [0,0,0]
for i in string:
    if i.isalpha():
        res[0] += 1
    elif i in numbers:
        res[1] += 1
    elif i in chars:
        res[2] += 1
    else:
        pass
print(f'There are {num_words} word(s), {res[0]} alphabets, {res[1]} digits and {res[2]} special characters in the given string.')

    