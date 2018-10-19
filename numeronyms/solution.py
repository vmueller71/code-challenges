"""
Write a function n7m to create Numeronyms.
You have to detect long words and convert them into their numeronym counterparts. 
A numeronym is the shortening of a long word by only keeping the first 1-2 letters and the last letter, 
replacing everything in between with the number of letters removed. 
Also, it is always all lowercase, regardless of their placement in a sentence.

A vowel is any of aeiou. If the second letter is not a vowel, it is kept, otherwise it is part of the 
letters to replace.

If a word can't be shorten (less characters than the original), then it stays as it is, including upper case letters.

Example where the second letter is a vowel: Numeronym -> N (length of "umerony") m -> n7m
Example where the second letter is not a vowel: Translation -> tr (length of "anslatio") n -> tr8n
Example of a word that can't be shorten: This -> This

Given a sentence, replace all words (alphabetic sequences) into numeronyms if the result is shorter than the original word.

Example
For sentence = "Shorten this text.", the output should be
n7m(sentence) = "sh4n this t2t.".
"""

def n7m(s):
    import re
    a = re.split(r'(\w+)', s)
    return ''.join(n if len(n) < len(w) else w for w, n in zip(a, (
        w if not w.isalpha() or len(w) < 4 else
        w[0] + str(len(w) - 2) + w[-1] if w[1] in 'aeiou' else
        w[0:2] + str(len(w) - 3) + w[-1] for w in (w.lower() for w in a))))
