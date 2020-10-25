'''
| Write a program to show if the entered character is uppercase or lowercase.                 |
|---------------------------------------------------------------------------------------------|
| We use the input() function to receive input from the user and print() function to print it |
'''

n = input("Enter character \n")

if n.isalpha() and len(n)==1:
    if n.isupper():
        print(f"{n} is uppercase.")
    else:
        print(f"{n} is lowercase.")
else:
    print("Enter alphabets please...")