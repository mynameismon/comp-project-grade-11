'''
| Write a program to print first n odd numbers in descending order.                           |
|---------------------------------------------------------------------------------------------|
| We use the input() function to receive input from the user and print() function to print it |
'''

n = int(input("Enter n\n"))
num = 1
res = []

for i in range(n):
    res.append(num)
    num+=2

res = [str(i) for i in res]
print(" ".join(res[::-1]))
