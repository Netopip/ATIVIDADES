def maior_menor():
    lista = list()
    while True:
        numero = int(input('Digite um numero: '))
        if numero == 0:
            break
        elif numero > 0:
            lista.append(numero)
        else:
            print('Digite um numero inteiro positivo')

    if lista:
        maior = max(lista)
        menor = min(lista)
        print(f'O maior numero da lista é {maior})
        print(f'O menor numero da lista é {menor})

maior_menor()