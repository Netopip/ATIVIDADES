def mais_alto(jogadores, alturas):
    nome_alto = jogadores[0]
    altura_alto = alturas[0]
    for i in range(len(jogadores)):
        if alturas[i] > altura_alto:
            altura_alto = alturas[i]
            nome_alto = jogadores[i]
    return nome_alto, altura_alto

def media_altura(alturas):
    media = sum(alturas)/ len(alturas)
    return media


def jogadores_acima_media(media, jogadores,alturas):
    novos_nomes = []
    novas_alturas = []
    for i in range(len(alturas)):
        if alturas[i] > media:
            novas_alturas.append(alturas[i])
            novos_nomes.append(jogadores[i])
    return novos_nomes, novas_alturas
            


def main():
    jogadores = []
    alturas = []
    for i in range(12):
        nome = str(input().strip())
        jogadores.append(nome)
        altura = float(input().strip())
        alturas.append(altura)
    
    nome_alto, altura_alto = mais_alto(jogadores, alturas)
    media = media_altura(alturas)
    novos_nomes, novas_alturas = jogadores_acima_media(media, jogadores,alturas)
    print(f'JOGADOR MAIS ALTO DO TIME\n{nome_alto}\n{altura_alto:.2f}')
    print(f'ALTURA MÉDIA DO TIME\n{media:.2f}')
    print(f'JOGADORES MAIS ALTOS QUE A MÉDIA DO TIME')
    for i,j in zip(novos_nomes,novas_alturas):
        print(f'{i}\n{j:.2f}')
    
if __name__== '__main__':
    main()