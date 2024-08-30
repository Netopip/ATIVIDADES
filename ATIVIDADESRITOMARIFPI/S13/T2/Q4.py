def soma_cumulativa(lista_original):
    lista_criada = []
    lista_criada.append(lista_original[0])
    soma = lista_original[0]
    for i in lista_original[1:]:
        soma += i
        lista_criada.append(soma)
    return lista_criada


def main():
    lista_original = []
    while True:
        numero = int(input())
        if numero == 0:
            break
        else:
            lista_original.append(numero)

    lista_criada = soma_cumulativa(lista_original)
    print(lista_criada)

if __name__ == '__main__':
    main()
