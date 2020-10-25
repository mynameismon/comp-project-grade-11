'''
| 1+ x2 + x3 + x4 + x5 +…….. xn                                                               |
|---------------------------------------------------------------------------------------------|
| Usage of the formula                                                                        |
'''

n = int(input("Enter n\n"))
x = int(input("Enter x\n"))

res = 0
for i in range(n+1):
    res += x**i
print(res)
