"""
Title: Most frequently used words in a text
Source: https://www.codewars.com/kata/51e056fe544cf36c410000fb/python
DESCRIPTION:
Write a function that, given a string of text (possibly with punctuation and line-breaks), returns an array of the
top-3 most occurring words, in descending order of the number of occurrences.
Assumptions:
A word is a string of letters (A to Z) optionally containing one or more apostrophes (') in ASCII.
Apostrophes can appear at the start, middle or end of a word ('abc, abc', 'abc', ab'c are all valid)
Any other characters (e.g. #, \, / , . ...) are not part of a word and should be treated as whitespace.
Matches should be case-insensitive, and the words in the result should be lowercased.
Ties may be broken arbitrarily.
If a text contains fewer than three unique words, then either the top-2 or top-1 words should be returned, or an empty
array if a text contains no words.
"""


from collections import Counter


def top_3_words(text):

    cont = 0
    for i in range(0, len(text)):               #EXCESSÃO EM QUE NÃO HÁ LETRAS NA STRING
        if (ord(text[i]) < 65) or (ord(text[i]) > 90 and ord(text[i]) < 97) or (ord(text[i]) > 122):
            cont += 1
    if cont == len(text):
        return []

    text = list(text)

    for i in range(0, len(text)):
        if (ord(text[i]) < 65 and ord(text[i]) != 32 and ord(text[i]) != 39) or (ord(text[i]) > 90 and ord(text[i]) < 97) or (ord(text[i]) > 122):
            text[i] = " "

    text = ''.join(text)
    text = text.strip()
    listaMaisFreq = []
    text = text.lower()
    text = text.split()
    dicionarioText = Counter(text)

    for k in sorted(dicionarioText, key=dicionarioText.get, reverse=True):
        listaMaisFreq.append(k)
        if len(listaMaisFreq) == 3:
            break

    return listaMaisFreq


#MAIN
print(top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"))




