"""Write a Python program to remove duplicates from a list."""

list1= [1,2,3,4,5,6,6,5,3,2,10]

d=set()
for i in list1:
    d.add(i)
print(d)
