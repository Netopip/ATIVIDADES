'''Escreva um programa que leia, separadamente, dia, mês e ano da data atual. Leia, da mesma forma, a data de nascimento de uma pessoa, calcule e escreva a idade exata em anos'''
def calcular_idade(dia_atual,mes_atual,ano_atual,dia,mes,ano):
    idade = ano_atual - ano
    
    if (mes_atual < mes) or (mes_atual < mes and dia_atual < dia):
        idade -= 1
    
    return idade    
    

def main():
    dia_atual = int(input())
    mes_atual = int(input())
    ano_atual = int(input())
    dia = int(input())
    mes = int(input())
    ano = int(input())
    
    idade = calcular_idade(dia_atual,mes_atual,ano_atual,dia,mes,ano)
    print(idade)
    
if __name__ == '__main__':
    main()