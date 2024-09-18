def e_letra_e_numero (caractere):
    letraenu = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSUVWXYZ0123456789'
    return caractere in letraenu

def main():
    caractere = input()

    print(e_letra_e_numero(caractere))

if __name__ == "__main__":
    main()
    
