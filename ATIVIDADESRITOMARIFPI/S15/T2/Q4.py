'''A tabela abaixo demonstra a quantidade de vendas dos fabricantes de veículos durante o período de 2013 a 2018, em mil unidades.

Fabricante / Ano	2013	2014	2015	2016	2017	2018
Fiat	204	223	230	257	290	322
Ford	195	192	198	203	208	228
GM	220	222	217	231	245	280
Wolkswagen	254	262	270	284	296	330
Faça um programa que:

leia os dados da tabela pelo teclado;
leia um ano do período determine e exiba o fabricante que mais vendeu nesse ano;
determine e exiba o ano de maior volume geral de vendas.
determine e exiba a média anual de vendas de cada fabricante durante o período.
'''


def definir_matriz():
    matriz = [
        ['Fabricante/Ano',[2013, 2014, 2015, 2016, 2017, 2018]],
        ['Fiat'],
        ['Ford'],
        ['GM'],
        ['Wolkswagen']
    ]
    
    for i in range(1,5):
        linha = []
        for j in range(6):
            valor = int(input().strip())
            linha.append(valor)
        matriz[i].append(linha)
    
    return matriz
            
def mais_vendido_ano(matriz, ano):
    indice = matriz[0][1].index(ano)
    maior_venda = -1
    fabricante = ''    
    for i in range(1,5):
        venda_ano = matriz[i][1][indice]
        if venda_ano > maior_venda:
            maior_venda = venda_ano
            fabricante = matriz[i][0]
    
    return fabricante,maior_venda

def maior_volume_geral(matriz):
    venda_por_ano = [0] * 6
    for i in range(1,5):
        for j in range(6):
            venda_por_ano[j] += matriz[i][1][j]
    maior_venda_total =max(venda_por_ano)
    ano_maior_venda = matriz[0][1][venda_por_ano.index(maior_venda_total)]
    return ano_maior_venda, maior_venda_total
    
    
def media_anual_vendas(matriz):
    medias = []
    
    for i in range(1,5):
        soma_vendas = sum(matriz[i][1])
        media = soma_vendas / len(matriz[i][1])
        medias.append([matriz[i][0], round(media,2)])
        
    return medias

    
def main():
    
    matriz = definir_matriz()
    ano = int(input().strip())
    fabricante, maior_venda = mais_vendido_ano(matriz,ano)
    ano_maior_venda, maior_venda_total = maior_volume_geral(matriz)
    medias = media_anual_vendas(matriz)
    print(f'A fabricante que mais vendeu em {ano} foi a {fabricante} com {maior_venda} mil unidades.')
    print(f'O ano de maior volume geral de vendas foi {ano_maior_venda} com {maior_venda_total} mil unidades.')
    print(f'A média anual de vendas de cada fabricante entre 2013 e 2018 foi:')
    for i in medias:
        print(f'A {i[0]} vendeu em média {i[1]} unidades por ano.')
    
    
    
if __name__=='__main__':
    main()

