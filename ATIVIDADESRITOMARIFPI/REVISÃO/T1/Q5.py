'''O custo ao consumidor, de um carro novo, é a soma do custo de fábrica com a percentagem do distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que a percentagem do distribuidor seja de 28% e os impostos de 45%, escrever um algoritmo para ler o custo de fábrica de um carro e escrever o custo final ao consumidor.'''

def main():
    custo_fabrica = float(input())
    distribuidor = 28/100 * custo_fabrica
    imposto = 45/100 * custo_fabrica
    
    custo_final = custo_fabrica + distribuidor + imposto
    print(f'R$ {custo_final:.2f}')
    
if __name__ == '__main__':
    main()