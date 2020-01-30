"""3. Написать функцию вычисления факториала числа
3. Write a function for calculating the factorial of a number"""

def factorial_cal(number):
    factorial=1
    if number>0:
        for n in range(1,number+1):
            factorial=factorial*n
        return(factorial)
    else:
        return("Cannot be equal or less than 0")

print(factorial_cal(int(input("Enter a number: "))))