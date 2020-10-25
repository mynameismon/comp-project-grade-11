'''
| Write a program to generate 6 random numbers between 100 and 999 and then print their mean, median and mode. |
|--------------------------------------------------------------------------------------------------------------|
| Using the random module and the sorted() function                                                            |
'''

import random

n = [random.randint(101,999) for _ in range(6) ]

mean = sum(n)/len(n)
median = (sorted(n)[2] + sorted(n)[3])/2
mode = 3*median - 2*mean

print(f"Random numbers are {' , '.join([str(i) for i in n ])}")
print(f"Mean is {mean}")
print(f"Median is {median}")
print(f"Mode is {mode}")
