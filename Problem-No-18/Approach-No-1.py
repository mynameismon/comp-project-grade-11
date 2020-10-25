'''
| Write a program that reads a number of seconds and prints it in form: min and seconds       |
|---------------------------------------------------------------------------------------------|
| We use the input() function to receive input from the user and print() function to print it |
'''

n = int(input('Enter the number of seconds\n'))

if n<=59:
    print(f'{n} seconds')
else:
    rem = n%60
    m = (n - rem)/60
    print(f'{m} minutes and {rem} seconds') 
    