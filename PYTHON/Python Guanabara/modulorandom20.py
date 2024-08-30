import random

def ordem_apresentacao(a1, a2, a3):
    lista = [a1, a2, a3]
    random.shuffle(lista)
    return lista

def main():
    a1 = input('1° aluno:')
    a2 = input('2° aluno:')
    a3 = input('3° aluno:')

    resultado = ordem_apresentacao(a1, a2, a3)

    print(resultado)

if __name__ == "__main__":
    main()

