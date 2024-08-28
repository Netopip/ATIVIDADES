def main():
    pB = int(input())
    pA = int(input())
    natalidade_pA = (0.02)
    natalidade_pB = (0.03)
    tempo_ano = 0
    if pB > pA:
        pA,pB = pB, pA #se p ususario colocar os dados invertidos o programa inverte novamente
    while pB < pA:
        pA += int((pA * natalidade_pA))
        pB += int((pB * natalidade_pB))
        tempo_ano += 1

    print(tempo_ano)

if __name__ == '__main__':
    main()
