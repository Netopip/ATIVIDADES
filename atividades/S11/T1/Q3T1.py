def maior_menor():
    lista = list()
    while True:
        numero = int(input())
        if numero == 0:
            break
        elif numero > 0:
            lista.append(numero)
        else:
            print()

    if lista:
        maior = max(lista)
        menor = min(lista)
        print(maior)
        print(menor)

maior_menor()