"""
|-------------------------------------------|
| Problem 6: Write a program to find the    |
| factorial of a number                     |
|-------------------------------------------|
| Approach:                                 |
| First, we take in a number using the      |
| input() function. Then, we check if the   |
| number is a positive integer or not. Is it|
| is, then we use a for loop to keep        |
| multiplying all integers upto that number |
|-------------------------------------------|
"""
from math import ceil, sqrt, log, floor


num = int(input("Enter a number: "))
factorial_num = 1

if num < 0:
  print("No factorials for negative numbers")
else:
  primeNumbers = []

  if num >= 2:
    primeNumbers.append(2)
  
  for i in range(3, num + 1, 2):
    isPrime = True
    for j in range(2, ceil(sqrt(i)) + 1):
      if (i % j == 0):
        isPrime = False
    if isPrime:
      primeNumbers.append(i)
  
  for p in primeNumbers:
    for k in range(0, floor(log(num, p))):
      factorial_num *= p ** (floor(num / (p ** (k + 1))))
  
  print("The factorial is:", factorial_num)
