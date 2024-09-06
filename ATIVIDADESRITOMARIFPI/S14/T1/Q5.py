'''Foram anotados nomes, idades e alturas de 30 alunos. Faça um programa que determine quais alunos com mais de 13 anos possuem altura inferior à média de altura dos alunos.'''

def media_altura(alturas):
    media = sum(alturas)/len(alturas)
    return media

def alunos_maior_13(idades,nomes,alturas):
    nome_13 = []
    altura_13 = []
    for i in range(len(idades)):
        if idades[i] > 13:
            nome_13.append(nomes[i])
            altura_13.append(alturas[i])
    return nome_13,altura_13


def alunos_altura_inferior(nome_13,altura_13,media):
    nome_alunos_inferior = []
    for i in range(len(altura_13)):
        if altura_13[i] < media:
            nome_alunos_inferior.append(nome_13[i])
    return nome_alunos_inferior
    


def main():
    nomes = []
    alturas = list()
    idades = []
    for i in range(30):
        nome = str(input())
        nomes.append(nome)
        idade = int(input())
        idades.append(idade)
        altura = float(input())
        alturas.append(altura)
        
    media = media_altura(alturas)
    nome_13,altura_13 = alunos_maior_13(idades,nomes,alturas)
    nome_alunos_inferior = alunos_altura_inferior(nome_13,altura_13,media)
    print(f'MAIORES DE 13 ANOS COM ALTURA ABAIXO DA MÉDIA')
    for i in nome_alunos_inferior:
        print(i)
    
if __name__ == '__main__':
    main()
        