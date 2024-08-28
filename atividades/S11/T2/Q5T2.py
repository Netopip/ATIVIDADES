def conceito_aluno(n):
    if n >= 8.5 :
        conceito = 'A'
    elif n >= 7:
        conceito = 'B'
    elif n >= 5:
        conceito = 'C'
    elif n >= 4:
        conceito = 'D'
    else:
        conceito = 'E'
    return  conceito



def main():
    while True:
        nota = float(input())
        if nota > 10 or nota < 0:
            print('Nota inválida.')
        else:
            break

    resultado = conceito_aluno(nota)
    print(resultado)


if __name__ == '__main__':
    main()