"""
Title: Next bigger number with the same digits
Source: https://www.codewars.com/kata/55983863da40caa2c900004e/python

Create a function that takes a positive integer and returns the next bigger number that can be formed by rearranging
its digits. For example:
    12 ==> 21
    513 ==> 531
    2017 ==> 2071
If the digits can't be rearranged to form a bigger number, return -1:
    9 ==> -1
    111 ==> -1
    531 ==> -1
"""


def next_bigger(n):

    lista1 = []
    lista2 = []

    n = list(str(n))
    for i in range(0, len(n)):    #CONVERTENDO A STRING PARA INTEIRO
        n[i] = int(n[i])

    valorInicial = -8       #VALOR DE REFERENCIA ALEATORIO
    for i in range(len(n)-2, -1, -1):
        if n[i] < n[i+1]:
            valorInicial = n[i]
            ptoReferencia = i
            break

    if valorInicial == -8:     #SE NÃO HOUVER UM NUMERO CUJO ANTERIOR SEJA MENOR QUE O POSTERIOR, ENTÃO NÃO HÁ UM NUMERO MAIOR COM OS MESMOS DÍGITOS
        return -1

    ptoReferenciaFinal = 0
    valorFinal = n[ptoReferencia+1]
    for c in range(ptoReferencia+1, len(n)):
        if n[c] > valorInicial and n[c] <= valorFinal:
            valorFinal = n[c]
            ptoReferenciaFinal = c

    n[ptoReferencia] = valorFinal
    n[ptoReferenciaFinal] = valorInicial

    for i in range(ptoReferencia+1, len(n)):
        lista2.append(n[i])
    lista2.sort()

    for i in range(0, ptoReferencia+1):
        lista1.append(n[i])

    listaFinal = lista1 + lista2

    for i in range(0, len(listaFinal)):
        listaFinal[i] = str(listaFinal[i])
    listaFinal = int(''.join(listaFinal))
    return listaFinal


#MAIN
print(next_bigger(4506))
