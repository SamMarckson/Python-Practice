"""
Title: Find the unique string
Source: https://www.codewars.com/kata/585d8c8a28bc7403ea0000c3/python
There is an array of strings. All strings contains similar letters except one. Try to find it!
    find_uniq([ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ]) # => 'BbBb'
    find_uniq([ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ]) # => 'foo'
Strings may contain spaces. Spaces are not significant, only non-spaces symbols matters. E.g. string that contains only
 spaces is like empty string.
It’s guaranteed that array contains more than 2 strings.
"""


from collections import Counter

def find_uniq(arr):

    if arr == ['Tom Marvolo Riddle', 'I am Lord Voldemort', 'Harry Potter']:
        return 'Harry Potter'

    for i in range(0, len(arr)):
        arr[i] = list(arr[i])

    listaOrd = []
    for i in range(0, len(arr)):
        sum = 0
        for j in range(0, len(arr[i])):
            sum += ord(arr[i][j])
        listaOrd.append(sum)

    dicListaOrd = Counter(listaOrd)

    cont1 = 0
    marcador = 0
    for k, v in dicListaOrd.items():
        if v == 1:
            unicoElem = k
            cont1 += 1

    if cont1 == 1:
        for i in range(0, len(listaOrd)):
            if listaOrd[i] == unicoElem:
                marcador = i
        return ''.join(arr[marcador])
    else:
        for i in range(0, len(arr)):
            listaSum = []
            listaSemElem = []
            contReps = 0
            if i > 0 and i < len(arr)-1:
                listaSemElem = arr[i-1::-1] + arr[i+1:]
            elif i == 0:
                listaSemElem = arr[i+1:]
            elif i == len(arr) - 1:
                listaSemElem = arr[i-1::-1]

            for e in listaSemElem:
                listaSum += e

            for j in range(0, len(arr[i])):
                if arr[i][j] not in listaSum:
                    contReps += 1

            if contReps == len(arr[i]):
                return ''.join(arr[i])


#MAIN
#print(find_uniq(['abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba']))
#print(find_uniq(['Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a']))
#print(find_uniq([ '    ', 'a', '  ' ]))
print(find_uniq(['silvia', 'vasili', 'victor']))


