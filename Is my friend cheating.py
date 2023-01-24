"""
Title: Is my friend cheating?
Source: https://www.codewars.com/kata/5547cc7dcad755e480000004/python

A friend of mine takes the sequence of all numbers from 1 to n (where n > 0).
Within that sequence, he chooses two numbers, a and b.
He says that the product of a and b should be equal to the sum of all numbers in the sequence, excluding a and b.
Given a number n, could you tell me the numbers he excluded from the sequence?
The function takes the parameter: n (n is always strictly greater than 0) and returns an array with all (a, b)
which are the possible removed numbers in the sequence 1 to n.
It happens that there are several possible (a, b). The function returns an empty array if no possible numbers are
found which will prove that my friend has not told the truth!
"""


def remov_nb(n):
    somaTotal = (n*(n + 1)) // 2
    listaExcluidos = []

    for b in range(n, 0, -1):
        a = (somaTotal - b) // (b + 1)

        if a <= n and a*b == somaTotal - (a + b):
            listaExcluidos.append((a, b))

    return listaExcluidos


#MAIN
print(remov_nb(26))