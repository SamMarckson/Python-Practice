from time import sleep

def contador(i, f, p):
    print(f"Contagem de {i} até {f} de {p} em {p}")
    sleep(2.5)
    if i<f:
        cont = i
        while cont <= f:
            print(f"{cont} ", end="", flush=True)
            sleep(0.5)
            cont += p
        print("FIM!")
    elif i>f:
        cont = i
        while cont >= f:
            print(f"{cont} ", end="", flush=True)
            sleep(0.5)
            cont += -p
        print("FIM!")

# MAIN
contador(1,10,1)
print()
contador(10,0,2)
print()
inicio = int(input("Digite o inicio: "))
fim = int(input("Digite o fim: "))
passo = int(input("Digite o passo: "))
contador(inicio, fim, passo)