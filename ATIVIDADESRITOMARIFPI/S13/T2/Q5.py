def esta_ordenada(lista):
    return lista == sorted(lista)#verifica se a lista digitada é igual a ela mesma na ordem crescente.

def main():
    lista = []
    n = int(input())
    for i in range(n):
        numero = input()#a entrada será uma string
        try:
           numero = float(numero)#tentativa de transformar em numero de ponto flutuante(float)
        except ValueError:
            pass
        lista.append(numero)#adicionando o numero a lista.

    if esta_ordenada(lista): # verifica se a lista esta ordenada.
        print('LISTA ORDENADA')
    else:
        print('LISTA NÃO ORDENADA')

if __name__ == '__main__':
    main()
