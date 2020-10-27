"""
_____________________________________________
|Problem : Write a program to compute simple|
|interest and compound interest given       |
|principle,rate and time period.            |
|-------------------------------------------|
| Approach:                                 |
| We use the input() function to receive    |
| input from the user and the print()       |
| function to print it.                     |
|-------------------------------------------|
"""
#Solution :-

p = float(input("Please enter Principal amount:\n"))
r = float(input("Please enter rate:\n"))
t = float(input("Please enter time:\n"))

sc = input('Simple interest or compund interest?[s/c]:  ')
while True:
    if(sc == 'c' or sc == 'C'):
        amount = p*(1 + r/100)**t
        interest = amount-p
        print(f"Interest is {interest} and amount is {amount}")
        break
    elif(sc=='s' or sc == 'S' ):
        interest = p*r*t/100
        amount = p + interest
        print(f"Interest is {interest} and amount is {amount}")
        break
    else:
        sc = input("Simple interest or compound interest?[s/c]:  ")
