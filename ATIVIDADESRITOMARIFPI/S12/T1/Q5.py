def main():

    ano = 1600 -1
    populacao_inicial = int(input())
    populacao_atual = populacao_inicial

    while populacao_atual >= populacao_inicial * 0.1:
        ano += 1
        mortes = (populacao_atual * 0.06)
        nascimento = (populacao_atual * 0.01)
        populacao_atual = populacao_atual - mortes + nascimento

        print(f"{round(ano)},{round(nascimento)},{round(mortes)},{round(populacao_atual)}")

if __name__ == '__main__':
    main()
