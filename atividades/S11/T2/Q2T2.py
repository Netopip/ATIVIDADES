def calcular_numeros(lista):
    numero_pessoas = len(lista)
    media = sum(lista) / numero_pessoas
    menor =min(lista)
    maior = max(lista)
    return numero_pessoas,media,menor,maior

def main():
    lista = []
    while True:
        idade = int(input())
        if idade > 0:
            lista.append(idade)
        elif idade < 0:
            print()
            continue
        elif idade == 0:
            break
            continue
    numero_pessoas,media,menor,maior = calcular_numeros(lista)
    print(f'{numero_pessoas}\n{media:.2f}\n{menor}\n{maior}')

if __name__ == '__main__':
    main()
