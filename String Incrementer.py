"""
Title: String incrementer
Exercise Source: https://www.codewars.com/kata/54a91a4883a7de5d7800009c/python

Your job is to write a function which increments a string, to create a new string.
If the string already ends with a number, the number should be incremented by 1.
If the string does not end with a number. the number 1 should be appended to the new string.
Examples:
    foo -> foo1
    foobar23 -> foobar24
    foo0042 -> foo0043
    foo9 -> foo10
    foo099 -> foo100
Attention: If the number has leading zeros the amount of digits should be considered.
"""

def increment_string(strng):
    listaNumeral = []
    listaRestante = []
    listaFinal = []

    indiceDeParada = 0


    for i in range(len(strng)-1, -1, -1):
        if ord(strng[i]) < 48 or ord(strng[i]) > 57:
            indiceDeParada = i
            break
        else:
            listaNumeral.insert(0, int(strng[i]))


    for j in strng[indiceDeParada::-1]:
        listaRestante.insert(0, j)
    listaRestante = "".join(listaRestante)


    if len(listaRestante) == 1 and len(listaNumeral) > 0:
        tam = len(listaNumeral) - 1
        listaNumeral[tam] += 1  # ADICIONANDO 1 AO ULTIMO ALGARISMO
        somador = 0

        for i in range(tam, -1, -1):
            listaNumeral[i] += somador
            somador = 0
            if listaNumeral[i] > 9 and i == 0:
                somador += 1
                # i -= somador
                listaNumeral[i] = 0
                listaFinal.insert(0, listaNumeral[i])  # ou listaFinal.append(listaNumeral[i]) ??????????
                listaFinal.insert(0, 1)
            elif listaNumeral[i] > 9 and i > 0:
                somador += 1
                listaNumeral[i] = 0
                listaFinal.append(listaNumeral[i])
            else:
                listaFinal.insert(0, listaNumeral[i])
        for i in range(0, len(listaFinal)):
            listaFinal[i] = str(listaFinal[i])
        listaFinal = "".join(listaFinal)

        return listaFinal


    if len(listaNumeral) == 0:
        listaRestante += '1'
        return listaRestante


    if len(listaNumeral) > 0:  # SE HOUVER NUMEROS
        tam = len(listaNumeral) - 1
        listaNumeral[tam] += 1  # ADICIONANDO 1 AO ULTIMO ALGARISMO
        somador = 0

        for i in range(tam, -1, -1):
           listaNumeral[i] += somador
           somador = 0
           if listaNumeral[i] > 9 and i == 0:
               somador += 1
               # i -= somador
               listaNumeral[i] = 0
               listaFinal.insert(0,listaNumeral[i])        # ou listaFinal.append(listaNumeral[i]) ??????????
               listaFinal.insert(0,1)
           elif listaNumeral[i] > 9 and i > 0:
               somador += 1
               listaNumeral[i] = 0
               listaFinal.append(listaNumeral[i])
           else:
               listaFinal.insert(0, listaNumeral[i])



        for i in range(0, len(listaFinal)):
            listaFinal[i] = str(listaFinal[i])
        listaFinal = "".join(listaFinal)

        return listaRestante + listaFinal


# MAIN
print(increment_string('fo99obar99'))