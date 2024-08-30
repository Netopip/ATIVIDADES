import random

def sorteio(a1, a2, a3):
    lista = [a1 , a2, a3]
    escolhido = random.choice(lista)
    return escolhido

def main():

    a1 = input('Digite o nome do aluno:')
    a2 = input('Digite o nome do 2 aluno:')
    a3 = input('Digite o nome do 3 aluno:')

    resultado = sorteio(a1, a2, a3)

    print(f'O escolhido para dar a bunda é {resultado}')

if __name__ == "__main__":
    main()

