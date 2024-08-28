def calcular_media():
    soma = 0
    contador = 0

    while True:
        numero = int(input())

        if numero == 0:
            break

        if numero > 0:
            soma += numero
            contador += 1
        else:
            print()

    if contador > 0:
        media = soma / contador
        print(f'{media:.2f}')
    else:
        print()

calcular_media()
