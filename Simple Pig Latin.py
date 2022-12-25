"""
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks
 untouched.
E.g.:
    pig_it('Pig latin is cool') # igPay atinlay siay oolcay
    pig_it('Hello world !')     # elloHay orldway !
"""


def pig_it(text):
    novaMatriz = []
    outraNovaMatriz = []
    lista = text.split()
    #print(lista)

    matriz = [list(palavra) for palavra in lista]
    #print(matriz)

    for i in range(0, len(matriz)):
        aux = matriz[i][0]
        for j in range(1, len(matriz[i])):
            novaMatriz.append(matriz[i][j])
        novaMatriz.append(aux)
        novaMatriz.append("ay")
        novaMatriz.append(" ")
    #print(f"Nova matriz = {novaMatriz}")

    for i in range(0, len(novaMatriz)):
        outraNovaMatriz.append(novaMatriz[i])
        if novaMatriz[i] == '!' or novaMatriz[i] == '?':
            break

    #print(f"Outra Nova Matriz = {outraNovaMatriz}")
    # novaMatriz = "".join(novaMatriz)
    # print(novaMatriz)
    #print(f"Outra Nova Matriz = {outraNovaMatriz}")
    outraNovaMatriz = "".join(outraNovaMatriz)
    outraNovaMatriz = outraNovaMatriz.rstrip()

    return outraNovaMatriz



#MAIN
#print(pig_it('Hello world !'))
print(pig_it('Pig latin is cool'))
#print(pig_it('Quis custodiet ipsos custodes ?'))