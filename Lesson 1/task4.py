"""4. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. 
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2"""

def word_match(list1):
    counter = 0
    for w in list1:
        if len(w)>=2 and w[0] == w[-1]:
            counter +=1
    return counter

print(word_match(['abc', 'xyz', 'aba', '1221']))