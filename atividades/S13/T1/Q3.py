def main():
    n = int(input())
    if n == 0:
        print('[]')
        print('[]')
        print("SEM NOTAS")
        print('0')
        print('[]')
        return

    lista = []
    for a in range(n):
        numero1 = float(input())
        lista.insert(0, numero1)
    print(f'{lista}')

    lista2 = []
    for b in range(n):
        numero2 = float(input())
        lista2.append(numero2)
    if lista2 :
        media = sum(lista2)/len(lista2)
        print(f'{lista2}\n{media:.1f}')
    else:
        print('SEM NOTAS')


    consoantes = []
    vogais = 0
    for i in range(n):
        letra = str(input()).strip()
        if letra.isalpha():
            if letra in 'AaEeIiOoUu':
                vogais +=1
            elif letra.isnumeric():
                continue
            else:
                consoantes.append(letra)
    print(f"{vogais}")
    print(f'{consoantes}')


if __name__ == '__main__':
    main()