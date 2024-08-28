def simulacao(salario,divida,mes,ano):
    while salario >= divida:
        divida = divida + (divida * 0.15)

        if mes == 3:
            salario = salario + (salario * 0.05)

        mes += 1
        if mes >12:
            mes = 1
            ano += 1

    return mes, ano

def main():
    salario0 = float(input('Digite o salario de Pedro: R$ '))
    divida0 = float(input('Agora digite a dívida que Pedro tem: R$ '))

    mes0 = 10
    ano0 = 2016

    mes,ano = simulacao(salario0, divida0, mes0, ano0)
    print(f'A divida de Pedro superará o seu salario no mês {mes}/{ano}')

if __name__ == '__main__':
    main()