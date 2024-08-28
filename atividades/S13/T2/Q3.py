def retornar_indices(listas_notas):
    nova_lista = []
    for i in range(len(listas_notas)):#no range do len de notas,[0][1][2][3], o len retorna 0,1,2,3,4 o total de notas que ha na lista
        if listas_notas[i] >= 6: # verifica se o índice na lista de notas é maior que 6.
            nova_lista.append(i)
    return nova_lista


def main():
    lista_notas = []
    for i in range(50):
        notas = float(input())
        lista_notas.append(notas)

    nova_lista = retornar_indices(lista_notas)
    print(f'{nova_lista}')


if __name__ == '__main__':
    main()
