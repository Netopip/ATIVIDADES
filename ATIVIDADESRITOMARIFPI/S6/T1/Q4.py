def main():
    numeros = []  

    for i in range(5):
        numero = int(input())
        numeros.append(numero)  

    maior_numero = max(numeros)
    menor_numero = min(numeros)

    soma = sum(numeros)
    media = soma / len(numeros)

    print(maior_numero)
    print(menor_numero)
    print(media)

if __name__ == "__main__":
    main()
