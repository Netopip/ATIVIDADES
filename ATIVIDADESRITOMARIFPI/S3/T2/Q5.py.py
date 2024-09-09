def calculo_bonificacao(tempo,valor):

    bonificacao = tempo * valor

    return bonificacao

def main():
    tempo = int(input())

    valor = float(input())

    bonificacao = calculo_bonificacao(tempo,valor)

    print(f"{bonificacao:.2f}")

if __name__ == "__main__":
    main()
