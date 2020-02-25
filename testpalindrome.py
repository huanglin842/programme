#!/usr/bin/env python3
def palindrome(s):
    return s == s[::-1]
s = input("Enter a string: ")
if palindrome(s):
    print("Yay a palindrome")
else:
    print("Oh no, not a palindrome")
