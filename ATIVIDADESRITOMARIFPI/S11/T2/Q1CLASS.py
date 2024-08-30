def calcular_conjunto(lista):
    soma = sum(lista)
    return soma


def main():
    lista = list()
    while True:
        numero = int(input('Digite um numeor interio: '))
        if numero == 0:
            break
        if numero > 0:
            lista.append(numero)
        elif numero < 0:
            print('Numero invalido!')
            continue
    soma = calcular_conjunto(lista)
    print(f'A soma dos numeros contino no conjunto é {soma}.')

if __name__ == '__main__':
    main()

