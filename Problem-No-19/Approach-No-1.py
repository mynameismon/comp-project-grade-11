'''
| Write a program to input a string and a character and count the number of occurrences of the input character in a given string |
|--------------------------------------------------------------------------------------------------------------------------------|
| Usage of the count() function                                                                                                  |
'''

string = input("Enter the string\n")
char   = input("Enter the character\n")
string = string.lower(); char = char.lower()
print(f'"{char}" appears in "{string}" {string.count(char)} time(s)')
