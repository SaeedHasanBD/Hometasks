""""Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x). 
Sample Dictionary ( n = 5) :
Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25} """

def dictionary1(number1):
    dict1=dict()
    for x in range(1,number1+1):
        dict1[x]=x*x
    print(dict1)

dictionary1(int(input("Enter a number except 0: ")))