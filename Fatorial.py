def funcFat(x):
    fat = 1
    if x == 1 or x == 0:
        fat = 1
        return fat
    else:
        for i in range(x, 0, -1):
            fat *= i
        return fat


# MAIN

n = int(input("Qual numero vc deseja calcular o fatorial? "))
print(funcFat(n))