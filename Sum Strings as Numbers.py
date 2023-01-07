"""
DESCRIPTION:
Given the string representations of two integers, return the string representation of the sum of those integers.
For example:
sumStrings('1','2') // => '3'
A string representation of an integer will contain no characters besides the ten numerals "0" to "9".
I have removed the use of BigInteger and BigDecimal in java
Python: your solution need to work with huge numbers (about a milion digits), converting to int will not work.
"""


def sum_strings(x, y):
    if (x == '0' and y == '0') or (x == '' and y == '') or (x == '0' and y == ''):
        return '0'

    listaX = list(x)
    listaZerosX = []
    listaY = list(y)
    listaZerosY = []

    if len(listaX) - len(listaY) > 0:           #IGUALANDO A QTD DE TERMOS, CASO LEN(X) > LEN(Y)
        tamY = len(listaY)
        while tamY < len(listaX):
            listaZerosY.append('0')
            tamY += 1
        listaY = listaZerosY + listaY
    if len(listaY) - len(listaX) > 0:           #IGUALANDO A QTD DE TERMOS, CASO LEN(Y) > LEN(X)
        tamX = len(listaX)
        while len(listaY) > tamX:
            listaZerosX.append('0')
            tamX += 1
        listaX = listaZerosX + listaX

    for i in range(0, len(listaX)):             #TRANSFORMANDO CADA ELEMENTO DA LISTA DE STR PARA INT
        listaX[i] = int(listaX[i])
        listaY[i] = int(listaY[i])

    listaSomas = []
    quociente = 0

    for i in range(len(listaX) - 1, -1, -1):    #SOMANDO TERMO A TERMO
        soma = listaX[i] + listaY[i] + quociente
        if soma > 9 and i > 0:
            quociente = soma // 10
            listaSomas.append(soma % 10)
        elif soma > 9 and i == 0:
            quociente = soma // 10
            listaSomas.append(soma % 10)
            listaSomas.append(quociente)
        elif soma <= 9:
            listaSomas.append(soma)
            quociente = 0

    listaSomas.reverse()

    if listaSomas[0] == 0:                      #REMOVENDO ZERO A ESQUERDA, CASO HAJA
        listaSomas.remove(listaSomas[0])

    for i in range(0, len(listaSomas)):
        listaSomas[i] = str(listaSomas[i])
    listaSomas = ''.join(listaSomas)

    return listaSomas


# MAIN
print(sum_strings('800', '9567'))