"""
_____________________________________________
|Problem : Write a program to perform       |
|          sorting on the given list of     |
|          strings, on the basis of length  |
|          of strings                       |
|-------------------------------------------|
| Approach:                                 |
|           Using the Bubble-sort algorithm | 
|           used in problem 36 with length  | 
|           of string as mode of comparision|
|-------------------------------------------|
"""

sample_list = ['the','quick','brown','fox','jumps','over','the','lazy', 'dog']

if len(sample_list)>1:
    for _ in range(len(sample_list)):
        for i in range(len(sample_list)-1):
            if len(sample_list[i]) > len(sample_list[i+1]):
                sample_list[i],sample_list[i+1] = sample_list[i+1],sample_list[i]
    print(sample_list)
else:
    print(sample_list)
