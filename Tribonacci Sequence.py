"""
But what if we started with [0, 0, 1] as a signature? As starting with [0, 1] instead of [1, 1] basically shifts the
common Fibonacci sequence by once place, you may be tempted to think that we would get the same sequence shifted by 2
places, but that is not the case and we would get: [0, 0, 1, 1, 2, 4, 7, 13, 24, ...]
Well, you may have guessed it by now, but to be clear: you need to create a fibonacci function that given a signature
array/list, returns the first n elements - signature included of the so seeded sequence.
Signature will always contain 3 numbers; n will always be a non-negative number; if n == 0, then return an empty array
(except in C return NULL) and be ready for anything else which is not clearly specified ;)
"""

def tribonacci(signature, n):
    listaRetorno = []
    if n != 0 and n >= 3:
        listaRetorno = signature[0:3]
        i = 3
        tam = len(listaRetorno)-1
        while i<n:
            listaRetorno.append(listaRetorno[tam] + listaRetorno[tam-1] + listaRetorno[tam-2])
            tam = len(listaRetorno) - 1
            i += 1
        return listaRetorno
    elif n != 0 and n > 0 and n < 3:
        for i in range(0, n):
            listaRetorno.append(signature[i])
        return listaRetorno
    else:
        return listaRetorno


#MAIN
print(tribonacci([1, 1, 1], 10))