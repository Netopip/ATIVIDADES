def e_consoante(caractere):
    consoantes = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSVWXYZ'
    return caractere in consoantes

def main():
    caractere = input()

    print(e_consoante(caractere))

if __name__ == "__main__":
    main()
    
