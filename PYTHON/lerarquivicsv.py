import csv

with open("c:/Users/ferna/OneDrive/Desktop/GIT/PYTHON/planilha.csv", "r") as arquivo :
    ler_arquivo = csv.reader(arquivo, delimiter=',')
    
    for i,linha in enumerate(ler_arquivo):
        if i == 0:
            print('cabeçalho: '+ str(linha))
        else:
            print('Valor: ' + str(linha))
    