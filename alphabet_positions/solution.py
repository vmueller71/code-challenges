"""
Write a program that sums the alphabet positions of the characters in a provided string
Characters are treated case insensitive.

examples:
sum_chars('ab') returns 3 (a=1, b=2)
sum_chars('AbCd') returns 10 (a=1, b=2, c=3, d=4)
sum_chars('Apli') returns 38
"""

def sum_chars(s):
    # Your code goes here
    x = 0
    for c in s:
        x += ord(c.lower()) - 96
    return x
