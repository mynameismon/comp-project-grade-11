'''
| 1+2+3... + n                                                                               |
|--------------------------------------------------------------------------------------------|
| Usage of the formula                                                                       |
'''

n = int(input("Enter last term\n"))

print(f'The sum of the series 1 + 2 + 3...n is {n*(n+1)/2}')
print(f'The sum of the series 1^2 + 2^2 + 3^2 ...n^2 is {n*(n+1)*(2*n+1)/6}')

sum = 0
x = int(input("Enter the value of x\n"))
for i in range(1, 7):
  factorial = 1
  for j in range(1, i + 1):
    factorial *= j
  
  sum += x ** i / factorial

print(f"The sum of the series x^1/1! + x^2/2! ... x^6/6! is {sum}")
print(f"The sum of the series 1 + x^2 + x^3...x^n is {(x^(n+1) - 1)/(x - 1)}")
