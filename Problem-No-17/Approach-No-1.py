'''
| Write a menu driven program to find the area of circle, square, rectangle & triangle.       |
|---------------------------------------------------------------------------------------------|
| We use the input() function to receive input from the user and print() function to print it |
'''

menu = input("For area of circle: 1,\nFor triangle: 2,\nFor square: 3,\nFor rectangle: 4\n")

if menu=='1':
    print("You chose circle...")
    r = float(input("Enter radius\n"))
    print(f'area is {3.14*r*r}')
elif menu=='2':
    print("You chose triangle...")
    b = int(input('Enter the base length\n'))
    h = int(input('Enter the height\n'))
    print(f'area is {0.5*b*h}')
elif menu=='3':
    print("You chose square...")
    s = int(input("Enter the side length\n"))
    print(f'area is {s*s}')
elif menu=='4':
    print("You chose rectangle")
    l = int(input("Enter the length\n"))
    b = int(input("Enter the breadth\n"))
    print(f"area is {l*b}")
else:
    print("Bad expression")