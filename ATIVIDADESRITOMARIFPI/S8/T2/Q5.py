'''Escreva um programa que leia o número de matrícula de um aluno, suas notas em 3 provas e a média das notas obtidas nos exercícios que fazem parte da sua avaliação. Calcule a média final usando a fórmula:

Média Final = (Nota 1 + Nota 2 * 2 + Nota 3 * 3 + Média Exercícios) / 7

A atribuição dos conceitos obedece a tabela abaixo.

Conceito	Média Final
A	>= 9.0
B	>= 7.5 e < 9.0
C	>= 6.0 e < 7.5
D	>= 4.0 e < 6.0
E	< 4.0
O programa deve escrever a matrícula do aluno, a média final, o conceito correspondente e a mensagem “Aprovado” se o conceito for A, B ou C ou “Reprovado” se o conceito for D ou E.

Mensagem	Conceitos
Aprovado	A, B ou C
Reprovado	D ou E
'''
def calcular_media(n1,n2,n3,media):
    media_total = (n1 + (n2*2) + (n3*3) + media) / 7
    return media_total

def conceito(media_total):
    if media_total >= 9:
        print(f'A\nAprovado')
    elif 9 > media_total >= 7.5:
        print(f'B\nAprovado')
    elif 7.5 > media_total >= 6:
        print(f'C\nAprovado')
    elif 6 > media_total >= 4:
        print(f'D\nReprovado')
    elif 4 > media_total:
        print('E\nReprovado')
    
def main():
    matricula = str(input())
    n1 = float(input())
    n2 = float(input())
    n3 = float(input())
    media = float(input())  
    
    media_total = calcular_media(n1,n2,n3,media)
    print(f'{matricula}\n{media_total:.2f}')
    conceito(media_total)
    
if __name__ == '__main__':
    main()
      