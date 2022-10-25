import random
def sorteio(lista):
    for i in range(0,5):
        n = random.randint(1,100)
        lista.append(n)
    print("NÚMEROS SORTEADOS: ", end="")
    print(lista)

def somaPar(lista):
    soma = 0
    for i in range(0, len(lista)):
        if lista[i] % 2 == 0:
            soma += lista[i]
    print(f"A SOMA DOS PARES É = {soma}")

# MAIN
numeros = list()
sorteio(numeros)
print("-"*50)
somaPar(numeros)