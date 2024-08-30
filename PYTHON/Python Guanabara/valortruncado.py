import math
def numero_int(numero):
    inteiro =math.trunc(numero)
    return inteiro
def main():
    
    numero = float(input('Digite um numero com ponto:'))
    parte_inteira = numero_int(numero)
    print(f'O valor inteiro do numero é {parte_inteira}')

if __name__ == "__main__":
    main()