"""
Write a function that accepts a sequence of comma separated binary numbers as a string and then checks whether they are divisible by 5 or not. 
The numbers that are divisible by 5 are to be returned as a comma separated string.

Examples:
divisible_by_5('0100,0011,1010,1001') returns '1010'
divisible_by_5('011,11110,1010') returns '11110,1010'

"""

def divisible_by_5(s):
    value = ''
    items=[x for x in s.split(',')]
    for p in items:
        intp = int(p, 2)
        if not intp % 5:
            value += str(p) + ','
    return value[:-1]
