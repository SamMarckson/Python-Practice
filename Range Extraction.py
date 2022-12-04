"""
A format for expressing an ordered list of integers is to use a comma separated list of either
individual integers
or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'.
The range includes all integers in the interval including both endpoints. It is not considered a range unless it spans
at least 3 numbers. For example "12,13,15-17"
Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted string
in the range format.
e.g.:
solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# returns "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"
"""
def solution(args):
    listaDisposicao = []
    listaSeq = []
    stringFinal = []

    if len(args) < 3:
        for i in range(0,len(args)):
            args[i] = str(args[i])
        args = ','.join(args)
        return args

    for i in range(2, len(args)):
        if args[i] - args[i-1] == 1 and args[i] - args[i-2] == 2:
            if args[i-2] not in listaDisposicao:
                listaDisposicao.append(args[i-2])
            if args[i-1] not in listaDisposicao:
                listaDisposicao.append(args[i-1])
            if args[i] not in listaDisposicao:
                listaDisposicao.append(args[i])
    # print(listaDisposicao)
    # print(len(listaDisposicao))
    if len(listaDisposicao) == 0:
        for i in range(0, len(args)):
            args[i] = str(args[i])
        args = ','.join(args)
        return args

    primeiro = listaDisposicao[0]
    c = 0
    tam = len(listaDisposicao)

    for i in range(1, len(listaDisposicao)):
        c += 1
        if listaDisposicao[i] - primeiro != c:
            ultimo = listaDisposicao[i-1]
            listaSeq.append(primeiro)
            listaSeq.append(ultimo)
            c = 0
            primeiro = listaDisposicao[i]
        if i == tam-1: #LENDO O ÚLTIMO ALGARISMO
            ultimo = listaDisposicao[i]
            listaSeq.append(primeiro)
            listaSeq.append(ultimo)

    output = [listaSeq[i:i+2] for i in range(0, len(listaSeq), 2)] #CRIANDO A LISTA E SUBLISTAS
    # print(output)

    for i in range(0, len(args)):  #ADICIONANDO OS QUE NÃO FAZEM PARTE DE INTERVALO ALGUM
        if args[i] not in listaDisposicao:
            output.append([args[i]])
    output.sort()

    for i in range(0, len(output)): #CONVERTENDO PARA STRING
        if len(output[i]) > 1:
            stringFinal.append(f"{output[i][0]}-{output[i][1]}")
        elif len(output[i]) == 1:
            stringFinal.append(f"{output[i][0]}")
    stringFinal = ','.join(stringFinal)
    return stringFinal


#MAIN
# print(solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]))
#print(solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]))
# print(solution([-3,-2,-1,2,10,15,16,18,19,20]))
#print(solution([1, 12, 15]))
#print(solution([1, 3, 5, 18, 24]))
print(solution([]))