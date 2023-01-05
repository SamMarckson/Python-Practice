"""
Write a function that takes a positive integer and returns the next smaller positive integer containing the same digits.
For example:
    next_smaller(21) == 12
    next_smaller(531) == 513
    next_smaller(2071) == 2017
Return -1 (for Haskell: return Nothing, for Rust: return None), when there is no smaller number that contains the same
digits. Also return -1 when the next smaller number with the same digits would require the leading digit to be zero.
    next_smaller(9) == -1
    next_smaller(135) == -1
    next_smaller(1027) == -1
*some tests will include very large numbers.
*test data only employs positive integers.
The function you write for this challenge is the inverse of this kata: "Next bigger number with the same digits."
"""


def next_smaller(n):

    lista1 = []
    lista2 = []

    n = list(str(n))
    for i in range(0, len(n)):    #CONVERTENDO A STRING PARA INTEIRO
        n[i] = int(n[i])

    valorInicial = -8       #VALOR DE REFERENCIA ALEATORIO
    for i in range(len(n)-2, -1, -1):
        if n[i] > n[i+1]:
            valorInicial = n[i]
            ptoReferencia = i
            break

    if valorInicial == -8:     #SE NÃO HOUVER UM NUMERO CUJO ANTERIOR SEJA MAIOR QUE O POSTERIOR, ENTÃO NÃO HÁ UM NUMERO MAIOR COM OS MESMOS DÍGITOS
        return -1

    ptoReferenciaFinal = 0
    valorFinal = n[ptoReferencia+1]
    for c in range(ptoReferencia+1, len(n)):
        if n[c] < valorInicial and n[c] >= valorFinal:
            valorFinal = n[c]
            ptoReferenciaFinal = c

    n[ptoReferencia] = valorFinal
    n[ptoReferenciaFinal] = valorInicial

    for i in range(ptoReferencia+1, len(n)):
        lista2.append(n[i])
    lista2.sort(reverse=True)

    for i in range(0, ptoReferencia+1):
        lista1.append(n[i])
    listaFinal = lista1 + lista2

    for i in range(0, len(listaFinal)):
        listaFinal[i] = str(listaFinal[i])
    if listaFinal[0] == '0':
        return -1
    else:
        listaFinal = int(''.join(listaFinal))
        return listaFinal


#MAIN
print(next_smaller(1))
