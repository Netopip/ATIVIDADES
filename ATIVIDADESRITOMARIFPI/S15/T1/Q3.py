'''Leia um dia e um mês como números inteiros distintos e informe as cidades que fazem aniversário nessa data. Veja o exemplo para o dia 9 e mês 2: CIDADES QUE FAZEM ANIVERSÁRIO EM 9 DE FEVEREIRO: São Miguel do Passa Quatro(GO) Centralina(MG) Itaporanga(PB) ...'''


def carrega_cidades():
    resultado = []
    with open('c:/Users/ferna/OneDrive/Desktop/GIT/ATIVIDADESRITOMARIFPI/S15/T1/cidades.csv', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            uf, ibge, nome, dia, mes, pop = linha.split(';')
            resultado.append(
                (uf, int(ibge), nome, int(dia), int(mes), int(pop))
            )
    arquivo.close()
    return resultado

def cidades_aniversariantes(resultado,dia,mes):
    cidades_an = []
    for cidade in resultado:
        if cidade[3] == dia and cidade[4]==mes:
            cidades_an.append(cidade)
    return cidades_an


def retornar_mes(mes):
    if mes == 1:
        return 'JANEIRO'
    elif mes == 2:
        return 'FEVEREIRO'
    elif mes == 3:
        return 'MARÇO'
    elif mes == 4:
        return 'ABRIL'
    elif mes == 5:
        return 'MAIO'
    elif mes == 6:
        return 'JUNHO'
    elif mes == 7:
        return 'JULHO'
    elif mes == 8:
        return 'AGOSTO'
    elif mes == 9:
        return 'SETEMBRO'
    elif mes == 10:
        return 'OUTUBRO'
    elif mes == 11:
        return 'NOVEMBRO'
    elif mes == 12:
        return 'DEZEMBRO'
    
    
def main():
    dia = int(input().strip())
    mes = int(input().strip())
    resultado = carrega_cidades()
    cidade_an = cidades_aniversariantes(resultado,dia,mes)
    mes = retornar_mes(mes)
    
    print(f'CIDADES QUE FAZEM ANIVERSÁRIO EM {dia} DE {mes}:')
    for cidade in cidade_an:
        print(f'{cidade[2]}({cidade[0]})')
    
    
if __name__ == '__main__':
    main()