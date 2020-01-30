"""1. Написать функцию, которая печатает квадраты всех нечетных чисел в произвольном интервале [0, Х]. А так же количество таких чисел.
1. Write a function that prints the squares of all odd numbers in an arbitrary interval [0, X]. As well as the number of such numbers."""

def square_count(x):
    count_odd = 0
    r = []
    for x in range(0, x):
        if x % 2!=0:
            count_odd += 1
            r.append(x ** 2)
    print(r)
    print("Number of odd numbers :", count_odd)

square_count(int(input("[0,x] Enter the x: ")))


