def contar_caracteres(frase):
    frase = frase.strip()
    
    numero_caracteres = len(frase)
    
    return numero_caracteres

def main():
   
    frase = input()
    
    numero_caracteres = contar_caracteres(frase)
    
    print(numero_caracteres)

if __name__ == "__main__":
    main()
