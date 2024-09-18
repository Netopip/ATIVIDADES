def verificar_caractere(caractere):
    if caractere.isdigit():
        return "número"
    elif caractere.isalpha():
        if caractere.lower() in 'aeiou':
            return "vogal"
        else:
            return "consoante"
    else:
        return "símbolo"
        

def main():

     caractere = input()

     verificacao = verificar_caractere(caractere)

     print(verificacao)

if __name__ == "__main__":
    main()
