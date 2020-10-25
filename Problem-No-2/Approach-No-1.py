"""
|-------------------------------------------|
| Problem 2: Write a program to convert     |
| temperature in Celsius to Fahrenheit      |
| & vice versa                              |
|-------------------------------------------|
| Approach:                                 |
|         We use the formula                |
|-------------------------------------------|
"""

temp = float(input("Enter Value: \n"))
convert = input("Convert to Celsius or Farenheit?[c/f]\n")

while True:
    if convert=='c':
        res = (temp - 32)/1.8
        print(f"Temperature in Celsius is {res}")
        break
    elif convert=='f':
        res = temp*1.8 + 32
        print(f"Temerature in Farhenheit is {res}")
        break
    else:
        convert = input("Convert to Celsius or Farenheit?[c/s]\n")

