"""Write a Python script to merge two Python dictionaries"""

def merge_dict(dict1,dict2):
    dict2.update(dict1)
    print(dict2)

dict1={'a': 1, 'b': 7}
dict2={'c': 3, 'd': 11}

merge_dict(dict1, dict2)