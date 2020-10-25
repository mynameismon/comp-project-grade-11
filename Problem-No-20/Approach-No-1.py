'''
| Write a program to count number of vowels in a given sentence                               |
|---------------------------------------------------------------------------------------------|
| We use the input() function to receive input from the user and print() function to print it |
'''

string = input("Enter please enter the string\n")
vowels = 'aeiouAEIOU'
res = 0
for i in string:
    if i in vowels:
        res += 1
print(f"Vowels appear in the string {res} time(s)")
