'''
| x – x2 /2! + x3 /3! – x4 /4! + x5 /5! – x6 /6! (Input x)                                    |
|---------------------------------------------------------------------------------------------|
| Usage of the formula                                                                        |
'''

x = int(input("Enter x\n"))
n = 7
summm = 1
term = 1
fct = 1
p = 1
multi = 1
    
for i in range(1, n): 
    fct = fct * multi * (multi+1) 
    p = p*x*x 
    term = (-1) * term 
    multi += 2
    summm = summm + (term * p)/fct 
    
print(summm)