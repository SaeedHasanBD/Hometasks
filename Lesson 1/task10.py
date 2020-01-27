"""Write a Python program to get the difference between the two lists"""

def Diff(list1, list2):
    list_dif= [i for i in list1 + list2 if i not in list1 or i not in list2]
    return list_dif

list1= [1,2,3,4,5,6,7,9]
list2= [1,4,6,7,3]
list3= Diff(list1,list2)
print(list3)