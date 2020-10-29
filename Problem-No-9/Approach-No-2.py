'''
| Write a program to find if a given number is prime or not.                                  |
|---------------------------------------------------------------------------------------------|
| We use the input() function to receive input from the user and print() function to print it |
'''

num = int(input("Enter a number: \n>> "))

if (num > 0):
  prime = True
  if (num % 2 == 0):
    prime = False
  else:
    for i in range(3, int(num ** 0.5) + 2, 2):
      if (num % i == 0):
        prime = False
  
  print("The number", num, "is", end=" ")
  if(not prime):
    print("not", end=" ")
  print("a prime number")

else:
  print("Please enter a positive number")