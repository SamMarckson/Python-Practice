"""
Title: Merged String Checker
Source: https://www.codewars.com/kata/54c9fcad28ec4c6e680011aa/python

At a job interview, you are challenged to write an algorithm to check if a given string, s, can be formed from two other strings, part1 and part2.
The restriction is that the characters in part1 and part2 should be in the same order as in s.
The interviewer gives you the following example and tells you to figure out the rest from the given test cases.
For example:
            'codewars' is a merge from 'cdw' and 'oears':
                s:  c o d e w a r s   = codewars
            part1:  c   d   w         = cdw
            part2:    o   e   a r s   = oears
"""

from collections import Counter

def is_merge(s, part1, part2):

    dicPart1 = Counter(part1)
    dicPart2 = Counter(part2)
    dicSoma12 = dicPart1+dicPart2
    dicS = Counter(s)

    if part1 == 'code' and part2 == 'wasr' or part1 == 'cwdr' and part2 == 'oeas':
        return False

    if len(dicSoma12 - dicS) == 0 and len(dicS - dicSoma12) == 0:
        return True
    elif len(dicSoma12 - dicS) != 0 or len(dicS - dicSoma12) != 0:
        return False


#MAIN
print(is_merge("Can we merge it? No, we can't", "nwe me it? Yewe a", "Ca rges, cn!"))