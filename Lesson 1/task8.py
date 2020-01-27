"""Write a Python program to find the highest 3 values in a dictionary
"""
from collections import Counter

dict_1={'a': 90, 'b': 34, 'c': 43, 'd':45, 'e': 54, 'f':12}

c= Counter(dict_1)
high_value= c.most_common(3)

for n in high_value:
    print(n[0],": ", n[1] )