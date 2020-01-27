"""1. You are asked to ensure that the first and last names of people begin with a capital letter in their passports.
For example, alison heck should be capitalized correctly as Alison Heck.
Given a full name, your task is to capitalize the name appropriately.
Input Format:A single line of input containing the full name, S.
Constraints:* 0 < len(S) < 1000*
The string consists of alphanumeric characters and spaces.
Note: in a word only the first character is capitalized.
Example 12abc when capitalized remains 12abc.
Output Format:Print the capitalized string, S."""
"""
def name_capitaliser(name):
    if 0<len(name)<1000:
        s=name.title()
        if s[0].isdigit():
            print(s.lower())
        else:
            print(s)

    else:
        print("Wrong input")


name_capitaliser(input("Write your first and last name: "))
"""

import string
def solve(s):
  string1=string.capwords(s, sep=" ")
  return string1

s=solve(input("Enter your full name: "))
print (s)