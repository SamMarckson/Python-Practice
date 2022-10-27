"""
Faça um Programa que leia dois vetores com 10 elementos cada.
Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.

"""

v1 = list()
v2 = list()
v3 = list()

for i in range(0,10):
    n1 = int(input(f"Insira o {i+1}o valor do primeiro vetor: "))
    v1.append(n1)

for i in range(0,10):
    n2 = int(input(f"Insira o {i+1}o valor do segundo vetor: "))
    v2.append(n2)

j1=0; j2=0
for i in range(0,20):
    if i%2 == 0:
        v3.append(v1[j1])
        j1 += 1
    elif i%2 != 0:
        v3.append(v2[j2])
        j2 += 1

print(v1)
print(v2)
print(v3)