def main():
    lista = []
    par = []
    impar = []
    for i in range(20):
        numero = int(input())
        if numero % 2 == 0:
            lista.append(numero)
            par.append(numero)
        else:
            lista.append(numero)
            impar.append(numero)
    print(f'{lista}\n{par}\n{impar}')

if __name__ == '__main__':
    main()
