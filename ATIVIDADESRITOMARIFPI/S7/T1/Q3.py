def verificar_sinal(cor):
    if cor == "V":
        return "Siga"
    elif cor == "A":
        return "Atenção"
    elif cor == "E":
        return "Pare"
    else:
        return "cor invalida"

def main():
    cor_do_sinal = input().upper()

    verificacao = verificar_sinal(cor_do_sinal)
    print(verificacao)

if __name__ == "__main__":
    main()

    
