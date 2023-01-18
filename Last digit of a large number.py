"""
Title: Last digit of a large number
Source: https://www.codewars.com/kata/5511b2f550906349a70004e1/python
"""


def last_digit(n1, n2):

    if (n2 == 0) or (n1 == 0 and n2 == 0):
        return 1

    listaDePadroes = []

    expo = 1
    strN1 = str(n1**expo)

    while True:
        if len(strN1) == 1:                 #LIDANDO COM ELEMENTOS DE TAMANHO 1
            listaDePadroes.append(n1**expo)
            expo += 1
            strN1 = str(n1 ** expo)
        else:
            break

    while True:                             #LIDANDO COM ELEMENTOS DE TAMANHO > 1
        ultimoDig = (n1**expo) % 10
        if ultimoDig not in listaDePadroes:
            listaDePadroes.append(ultimoDig)
            expo += 1
        else:
            break

    #print(listaDePadroes)
    resto = n2 % len(listaDePadroes)

    if resto == 0:
        return listaDePadroes[len(listaDePadroes) - 1]
    else:
        return listaDePadroes[resto - 1]


#MAIN
print(last_digit(2 ** 200, 2 ** 300))