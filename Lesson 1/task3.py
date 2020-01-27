"""Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string. 
Sample String : 'w3resource'
Expected Result : 'w3ce'
Sample String : 'w3'
Expected Result : 'w3w3'
Sample String : ' w'
Expected Result : Empty String"""

def string_concatinate(str1):
    if len(str1)>=2:
        new_str1=str1[:2]+str1[-2:]
        print(new_str1)
    else:
        print('')


string_concatinate(input("Enter string: "))

