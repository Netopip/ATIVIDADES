def e_letras(caractere):
    letras = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSUVWXYZ'
    return caractere in letras

def main():
    caractere = input()

    print(e_letras(caractere))

if __name__ == "__main__":
    main()
    
