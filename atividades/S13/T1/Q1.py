def calcular(lista):
    soma = sum(lista)
    multi = 1
    for num in lista: #O for num in lista: começa a iterar sobre cada elemento da lista. Aqui, num é uma variável que, a cada iteração, assume o valor do próximo elemento da lista.
        multi *= num
    return soma, multi

def main():
    lista = []
    while True:
        numero = int(input())
        if numero >= 0:
            lista.append(numero)
            if len(lista) == 10:
                break
            else:
                continue
    soma, multi = calcular(lista)
    print(f'{lista}\n{soma}\n{multi}')


if __name__ == '__main__':
    main()





