"""5. You are given with 3 sets, find if third set is a subset of the first and the second sets
Input: set([1,2]), set([2,3), set([2])
Expected result: True
Input: set([1,2]), set([3,4), set([5])
Expected result: False"""

set1= {1,2}
set2= {2,3}
set3= {2}

s=set3.issubset(set1) and set3.issubset(set2)
print(s)
