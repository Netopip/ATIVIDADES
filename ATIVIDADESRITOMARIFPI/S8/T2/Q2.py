'''Escreva um programa que leia um número inteiro. Mostre a soma dos dígitos para os números entre 0 (zero) e 100 mil ou -1 para outros valores. Por exemplo: Em 16.759 a soma dos dígitos é 1 + 6 + 7 + 5 + 9 = 31 é o valor retornado; Em 136.759 o valor lido é maior que 100 mil e deve retornar -1; Em -100 o valor lido é negativo e deve retornar -1.'''
def verificar_numero(numero):
    soma = 0
    if numero < 0 or numero > 100000:
        return -1
    return sum(int(digito) for digito in str(numero))
        
        
def main():
    valor = int(input())
    
    resultado = verificar_numero(valor)
    print(resultado)
    
if __name__ == '__main__':
    main()
    