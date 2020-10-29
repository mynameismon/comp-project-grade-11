'''
| Write a program to find a reverse of the four-digit number                                  |
|---------------------------------------------------------------------------------------------|
| We use the input() function to receive input from the user and print() function to print it |
'''
import math

num = int(input("Enter a number \n>> "))
revnum = 0

for i in range(1, int(math.log10(num)) + 2):
  revnum *= 10
  revnum += int(num % 10)
  num /= 10

print("The reversed number is", int(revnum))