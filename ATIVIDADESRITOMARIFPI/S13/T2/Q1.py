def multiplica_constante(lista):
    constante = int(input())
    lista2 = []
    for i in lista:
        i = i * constante
        lista2.append(i)
    return lista2


def main():
    lista = []
    while True:
        numero = int(input())
        if numero == 0:
            break
        else:
            lista.append(numero)
    lista2 = multiplica_constante(lista)
    print(f'{lista2}')

if __name__ == '__main__':
    main()