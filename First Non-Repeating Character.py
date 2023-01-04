"""
Title: First non-repeating character
Source: https://www.codewars.com/kata/52bc74d4ac05d0945d00054e/solutions/python

Write a function named first_non_repeating_letter that takes a string input, and returns the first character that is
not repeated anywhere in the string.
For example, if given the input 'stress', the function should return 't', since the letter t only occurs once in the
string, and occurs first in the string.
As an added challenge, upper- and lowercase letters are considered the same character, but the function should return
the correct case for the initial letter. For example, the input 'sTreSS' should return 'T'.
If a string contains all repeating characters, it should return an empty string ("") or None -- see sample tests.
"""

from collections import Counter

def first_non_repeating_letter(string):

    if len(string) == 0:
        return ''
    if len(string) == 1:
        return string

    contIguais = 0
    for i in range(0, len(string)):
        if string[i] == string[0]:
            contIguais += 1
    if contIguais == len(string) and len(string) > 1:
        return ''

    stringOriginal = string
    string = string.lower()
    string = list(string)

    c = Counter(string)

    elementoEscolhido = 0
    for k, v in c.items():
        if v == 1:
            elementoEscolhido = k
            break

    if elementoEscolhido == 0:   #INDICA QUE NÃO HÁ ELEMENTOS REPETIDOS
        return ''

    if elementoEscolhido in stringOriginal:
        return elementoEscolhido
    else:
        return elementoEscolhido.upper()


#MAIN
print(first_non_repeating_letter("MbqTcjcmx9. wYZLHyhjK;oq;Zkk8tHlb:sx7zIKS9gq3"))
