"""
_____________________________________________
|Problem : Write a program to sort a list   |
|          of integers using bubble sort.   |
|-------------------------------------------|
| Approach:                                 |
| The Bubble sort is a sorting algorithm    |
| that repeatedly steps through the list,   |
| compares adjacent elements and swaps them |
| if they are in the wrong order.           |
|-------------------------------------------|
"""

sample_list = [2,3,1,5,2,5,2,7,5,3,8,1,0,9]

if len(sample_list)>1:
    for _ in range(len(sample_list)):
        for i in range(len(sample_list)-1):
            if sample_list[i] > sample_list[i+1]:
                sample_list[i],sample_list[i+1] = sample_list[i+1],sample_list[i]
    print(sample_list)
else:
    print(sample_list)
