"""
Created on Fri Oct 30 19:25:57 2020

@author: bezbakri
"""

'''

|------------------------------|
| Problem: Write a program to  |
| read a list of ‘n’ integers  |
| from the user. Create two new|
| lists, one having all        |
| positive numbers and the     |
| other having all negative    |
| numbers.  Print all three    |
| lists.                       |
|------------------------------|
|
|------------------------------|

'''


n = []
while True:
    n_in = input("Enter some numbers. To exit, type exit: ")
    if n_in == "exit":
        break
    else:
        n.append(int(n_in))

nPos = []
nNeg = []

for i in n:
    if i>0:
        nPos.append(i)
    elif i<0:
        nNeg.append(i)

print(f"Original list = {n}")
print(f"Positive list = {nPos}")
print(f"Negative list = {nNeg}")
