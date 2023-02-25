"""
Title: Valid Parentheses
Source: https://www.codewars.com/kata/52774a314c2333f0a7000688/python
Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid. The
function should return true if the string is valid, and false if it's invalid.
Examples:
"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true
        Constraints
0 <= input.length <= 100
Along with opening (() and closing ()) parenthesis, input may contain any valid ASCII characters. Furthermore,
the input string may be empty and/or not contain any parentheses at all. Do not treat other forms of brackets as
parentheses (e.g. [], {}, <>).
"""


def valid_parentheses(string):

    onlyParenthesesString = []
    for i in range(0, len(string)):             #ELIMINANDO TODOS OS CARACTERES DIFERENTES DE '(' E ')'
        if ord(string[i]) == 40 or ord(string[i]) == 41:
            onlyParenthesesString.append(string[i])
    onlyParenthesesString = ''.join(onlyParenthesesString)

    qtdOpenP = 0
    qtdCloseP = 0
    for i in range(0, len(onlyParenthesesString)):
        if onlyParenthesesString[i] == '(':
            qtdOpenP += 1
        elif onlyParenthesesString[i] == ')':
            qtdCloseP += 1
        if qtdCloseP > qtdOpenP:
            return False

    if qtdOpenP == qtdCloseP:
        return True
    elif qtdOpenP > qtdCloseP:
        return False


#MAIN
print(valid_parentheses(""))