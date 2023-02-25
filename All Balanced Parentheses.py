"""
Title: All Balanced Parentheses
Source: https://www.codewars.com/kata/5426d7a2c2c7784365000783/python
Write a function which makes a list of strings representing all of the ways you can balance n pairs of parentheses
Examples:
    balanced_parens(0) => [""]
    balanced_parens(1) => ["()"]
    balanced_parens(2) => ["()()","(())"]
    balanced_parens(3) => ["()()()","(())()","()(())","(()())","((()))"]
"""


def balanced_parens(n):

    def generateParenthesis(openP, closeP, sample, answer):

        if openP == 0 and closeP == 0:
            answer.append(sample)
        if openP > closeP or openP < 0 or closeP < 0:   # not possible
            return

        sample += '('
        generateParenthesis(openP - 1, closeP, sample, answer)
        sample = sample[:-1]
        sample += ')'
        generateParenthesis(openP, closeP - 1, sample, answer)
        sample = sample[:-1]

    ans = []
    s = ""
    generateParenthesis(n, n, s, ans)
    return ans


#MAIN
print(balanced_parens(3))