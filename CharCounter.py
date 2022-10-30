"""
Faça um programa que conta quantos caracteres únicos existem em uma string.
A string 'Hello, world!' tem dez caracteres únicos, enquanto a string 'zzz' tem apenas um.
Utilize um dicionário para resolver esse problema.
"""

import collections
# from collections import Counter

letraUnit = 0
my_str = input("Insira uma string: ")
# contador = Counter(my_str)
contador = collections.Counter(my_str)
print(contador)
print()
for k in contador:
     if contador[k] != 0:
         letraUnit += 1
print(f"A quantidade de elementos distintos que aparecem na string é de: {letraUnit}")


