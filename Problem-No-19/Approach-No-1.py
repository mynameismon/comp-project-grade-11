'''
| Write a program to input a string and a character and count the number of occurrences of the input character in a given string |
|--------------------------------------------------------------------------------------------------------------------------------|
| We use the input() function to receive input from the user and print() function to print it                                    |
'''

string = input("Enter the string\n")
char   = input("Enter the character\n")
print(f'"{char}" appears in "{string}" {string.count(char)} time(s)')
