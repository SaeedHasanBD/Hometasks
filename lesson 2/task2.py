"""2. Написать функцию, которая принимает 3 числа (a,b,c) и проверяет сколько чисел между ‘a’ и ‘b’ делятся на ‘c’
2. Write a function that takes 3 numbers (a, b,c) and checks how many numbers between ‘a’ and ' b’ are divided by ‘c’"""

def count_D(a,b,c):
    counter=0
    for n in range(a,b):
        if (n%c==0):
            counter+=1
    return counter

a= 10
b=50
c=5

print(count_D(a,b,c))