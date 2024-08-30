def calcular_media():
    soma = 0
    contador = 0

    while True:
        numero = int(input('Digite um numero inteiro: '))

        if numero == 0:
            break

        if numero > 0:
            soma += numero
            contador += 1
        else:
            print('Digite um numero inteiro positivo!')

    if contador > 0:
        media = soma / contador
        print(f'A média dos numeros digitados é {media:.2f}')
    else:
        print()

calcular_media()
