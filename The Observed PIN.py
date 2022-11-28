"""
Alright, detective, one of our colleagues successfully observed our target person, Robby the robber.
We followed him to a secret warehouse, where we assume to find all the stolen stuff. The door to this warehouse is
secured by an electronic combination lock. Unfortunately our spy isn't sure about the PIN he saw, when Robby entered it.
The keypad has the following layout:
┌───┬───┬───┐
│ 1 │ 2 │ 3 │
├───┼───┼───┤
│ 4 │ 5 │ 6 │
├───┼───┼───┤
│ 7 │ 8 │ 9 │
└───┼───┼───┘
    │ 0 │
    └───┘
He also mentioned, he knows this kind of locks. You can enter an unlimited amount of wrong PINs, they never finally lock
the system or sound the alarm. That's why we can try out all possible (*) variations.
* possible in sense of: the observed PIN itself and all variations considering the adjacent digits
Can you help us to find all those variations?
"""
from itertools import product
def get_pins(observed):
    lista_num = []
    lista_possibilidade = []
    elemento = []

    for i in range(0, len(observed)):
        lista_num.append(observed[i])
    #print(lista_num)
    for i in range(0, len(lista_num)):
        if lista_num[i] == '1':
            lista_possibilidade.append('1')
            lista_possibilidade.append('2')
            lista_possibilidade.append('4')
        if lista_num[i] == '2':
            lista_possibilidade.append('2')
            lista_possibilidade.append('1')
            lista_possibilidade.append('3')
            lista_possibilidade.append('5')
        if lista_num[i] == '3':
            lista_possibilidade.append('3')
            lista_possibilidade.append('2')
            lista_possibilidade.append('6')
        if lista_num[i] == '4':
            lista_possibilidade.append('4')
            lista_possibilidade.append('1')
            lista_possibilidade.append('5')
            lista_possibilidade.append('7')
        if lista_num[i] == '5':
            lista_possibilidade.append('5')
            lista_possibilidade.append('2')
            lista_possibilidade.append('4')
            lista_possibilidade.append('6')
            lista_possibilidade.append('8')
        if lista_num[i] == '6':
            lista_possibilidade.append('6')
            lista_possibilidade.append('3')
            lista_possibilidade.append('5')
            lista_possibilidade.append('9')
        if lista_num[i] == '7':
            lista_possibilidade.append('7')
            lista_possibilidade.append('4')
            lista_possibilidade.append('8')
        if lista_num[i] == '8':
            lista_possibilidade.append('8')
            lista_possibilidade.append('5')
            lista_possibilidade.append('7')
            lista_possibilidade.append('9')
            lista_possibilidade.append('0')
        if lista_num[i] == '9':
            lista_possibilidade.append('9')
            lista_possibilidade.append('6')
            lista_possibilidade.append('8')
        if lista_num[i] == '0':
            lista_possibilidade.append('0')
            lista_possibilidade.append('8')
        elemento.append(lista_possibilidade[:])
        lista_possibilidade.clear()
    #print(elemento)
    senhas = elemento[0]
    for i in range(1, len(elemento)):
        senhas = [f'{s}{num}' for s, num in product(senhas, elemento[i])]
    return senhas


#MAIN
print(get_pins('369'))