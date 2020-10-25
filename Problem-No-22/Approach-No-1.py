'''
| Write a program to print first n odd numbers in descending order.                           |
|---------------------------------------------------------------------------------------------|
| We use the input() function to receive input from the user and print() function to print it |
'''

n = int(input("Enter n\n"))
res = [str(i) for i in range(n,0,-1) if i%2==1]
print(' '.join(res))