"""Write a Python program to count the number of characters (character frequency) in a string.
Sample String : google.com
Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}"""

def char_freq(string):
    freq= {}

    for c in string:
        key= freq.keys()

        if c in key:
            freq[c]+=1
        else:
            freq[c]=1
    return freq

print(char_freq(input("Enter your string: \n")))