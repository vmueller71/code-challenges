"""
Write the function question_marks(testString)  that accepts a string parameter, 
which will contain single digit numbers, letters, and question marks, 
and check if there are exactly 3 question marks between every pair of two 
numbers that add up to 10. 
If so, then your program should return the string true, otherwise it should 
return the string false. 
If there aren't any two numbers that add up to 10 in the string, then your 
program should return false as well. 

For example: if str is "arrb6???4xxbl5???eee5" then your program should 
return true because there are exactly 3 question marks between 6 and 4, and 
3 question marks between 5 and 5 at the end of the string. 


Sample Test Cases
Input:"arrb6???4xxbl5???eee5"
Output:"true"

Input:"aa6?9"
Output:"false"

Input:"acc?7??sss?3rr1??????5ff"
Output:"true"
"""

def question_marks(testString):
    # Your code goes here
    has_3_question_marks = False
    qm_found = 0
    start_int = None
    for c in testString:
        if c.isdigit():
            if start_int:
                if start_int + int(c) == 10:
                    if qm_found == 3:
                        has_3_question_marks = True
                    else:
                        return False
            start_int = int(c)
            qm_found = 0
        else:
            if c == '?':
                qm_found += 1

    return has_3_question_marks

