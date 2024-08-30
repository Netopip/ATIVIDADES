def main():
    distancia_vantagem = int(input())
    velocidade_tartaruaga = 1
    velocidade_lebre = 10
    distancia_t = distancia_vantagem
    distancia_l = 0
    tempo = 0
    while distancia_t > distancia_l:
        distancia_t += velocidade_tartaruaga
        distancia_l += velocidade_lebre
        tempo += 1
    print(tempo)

if __name__ == '__main__':
    main()

