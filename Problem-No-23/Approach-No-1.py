'''
| Write a program that should prompt the user to type some sentences. It should then print number of words, number of characters, number of digits and number of special characters in it. |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| We use the input() function to receive input from the user and print() function to print it                                                                                              |
'''

string = input("Enter a sentence...\n")
chars = '!@#$%^&*()<>?:-\"\'}+=_{|\][;//.,`~'
num_words = len(string.split())
res = [0,0,0,0]
for i in string:
    if i.isalpha():
        res[0] += 1
    elif i.isdigit():
        res[1] += 1
    elif i in chars:
        res[2] += 1
    else:
        res[3] +=1
print(f'There are {num_words} word(s), {res[0]} alphabets, {res[1]} digits, {res[2]} special characters and {res[3]} spaces in the given string.')
    
