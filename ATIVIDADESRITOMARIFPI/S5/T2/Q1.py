def e_vogal(caractere):
    vogais = 'aeiouAEIOU'
    return caractere in vogais

def main():
    caractere = input()

    print(e_vogal(caractere))

if __name__ == "__main__":
    main()
    
