'''
| Write a program to show if the entered character is uppercase or lowercase.                 |
|---------------------------------------------------------------------------------------------|
| Usage of isalpha(), islower() and isupper()                                                 |
'''

n = input("Enter character \n")

if n.isalpha() and len(n)==1:
    if n.isupper():
        print(f"{n} is uppercase.")
    else:
        print(f"{n} is lowercase.")
else:
    print("Enter alphabets please...")