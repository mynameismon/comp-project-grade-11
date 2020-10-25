'''
| 1+ x2 + x3 + x4 + x5 +…….. xn                                                               |
|---------------------------------------------------------------------------------------------|
| We use the input() function to receive input from the user and print() function to print it |
'''

n = int(input("Enter n\n"))
x = int(input("Enter x\n"))

res = 0
for i in range(n+1):
    res += x**i
print(res)
