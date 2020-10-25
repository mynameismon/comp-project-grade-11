'''
| Write a program that replaces all vowels in the with ‘* |
|---------------------------------------------------------|
| Using re module.                                        |
'''
import re
string = input("Enter the string\n")
print(re.sub('[aeiouAEIOU]','*',string))