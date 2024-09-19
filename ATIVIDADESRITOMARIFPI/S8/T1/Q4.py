'''Escreva um programa que leia 5 números inteiros, calcule e mostre a média e escreva os que são maiores que a média. Considere duas casas decimais.

'''
def media_lista(lista):
    media = sum(lista)/ len(lista)
    return media

def maior_media(media,lista):
    numeros_acima_media = []
    for i in lista:
        if i > media:
            numeros_acima_media.append(i) 
    return numeros_acima_media

def main():
    lista = []
    for i in range(5):
        n = int(input())
        lista.append(n)
        
    media = media_lista(lista)
    numeros_acima_media = maior_media(media,lista)
    print(f'{round(media,2)}')
    print(*numeros_acima_media, sep='\n')
    
if __name__=='__main__':
    main()