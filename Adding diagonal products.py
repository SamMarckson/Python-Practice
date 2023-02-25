"""
Title: #9 Matrices: Adding diagonal products
Source: https://www.codewars.com/kata/590bb735517888ae6b000012/python
We have a square matrix M of dimension n x n that has positive and negative numbers in the ranges [-9,-1] and [0,9],
(the value 0 is excluded).
We want to add up all the products of the elements of the diagonals UP-LEFT to DOWN-BOTTOM, that is the value ofsum1;
and the elements of the diagonals UP-RIGHT to LEFT-DOWN and that is sum2. Then, as a final result, the value of
sum1 - sum2.
E.g.
M = [[ 1,  4, 7,  6,  5],
     [-3,  2, 8,  1,  3],
     [ 6,  2, 9,  7, -4],
     [ 1, -2, 4, -2,  6],
     [ 3,  2, 2, -4,  7]]

So the value of sum1 - sum2 is equal to: 1164 - 66 = 1098
Create the code to do this calculation.
"""


def sum_prod_diags(matrix):

    # CÁLCULO DAS DIAGONAIS ACIMA DA DIAGONAL PRINCIPAL, INCLUINDO A DIAGONAL PRINCIPAL
    repsDiagSup = 0
    cont = 0
    prod1 = []
    while repsDiagSup < len(matrix):
        mult = 1
        for i in range(0, len(matrix) - cont):
            mult *= matrix[i][i+cont]
        prod1.append(mult)
        cont += 1
        repsDiagSup += 1

    # CÁLCULO DAS DIAGONAIS ABAIXO DA DIAGONAL PRINCIPAL
    repsDiagInf = 1
    cont = 1
    while repsDiagInf < len(matrix):
        mult = 1
        for i in range(0, len(matrix) - cont):
            mult *= matrix[i + cont][i]
        prod1.append(mult)
        cont += 1
        repsDiagInf += 1

    # CÁLCULO DAS DIAGONAIS ACIMA DA DIAGONAL SECUNDÁRIA, INCLUINDO A DIAGONAL SECUNDÁRIA
    repsDiagSupEsq = 0
    cont = 0
    prod2 = []
    while repsDiagSupEsq < len(matrix):
        mult = 1
        cont2 = 1 + repsDiagSupEsq
        for i in range(0, len(matrix) - cont):
            mult *= matrix[i][len(matrix) - cont2]
            cont2 += 1
        prod2.append(mult)
        cont += 1
        repsDiagSupEsq += 1

    # CÁLCULO DAS DIAGONAIS ABAIXO DA DIAGONAL SECUNDÁRIA
    repsDiagInfEsq = 1
    cont = 1
    while repsDiagInfEsq < len(matrix):
        mult = 1
        cont2 = repsDiagInfEsq
        cont3 = 1
        for i in range(0, len(matrix) - cont):
            mult *= matrix[cont2][len(matrix) - cont3]
            cont2 += 1
            cont3 += 1
        prod2.append(mult)
        cont += 1
        repsDiagInfEsq += 1

    return sum(prod1) - sum(prod2)


#MAIN
print(sum_prod_diags([[1,  4, 7,  6,  5],
                [-3,  2, 8,  1, 3],
                [6,  2, 9,  7, -4],
                [1, -2, 4, -2,  6],
                [3,  2, 2, -4,  7]]))