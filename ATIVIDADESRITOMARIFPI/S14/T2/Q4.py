'''Escreva um programa que ler dois conjuntos de números reais, armazenando-os em listas e calcule o produto escalar entre eles. Os conjuntos têm 5 elementos cada. Imprimir os dois conjuntos e o produto escalar, sendo que o produto escalar e dado por: (x1*y1 )+(x2*y2 )+(x3*y3 )+⋯+(xn*yn). Por exemplo, para as duas listas X e Y a seguir:

        0       1       2       3       4
X =     2       5       7       3       9

Y =     3       8       1       0       4
O produto escalar será: (2 x 3) + (5 x 8) + (7 x 1) + (3 x 0) + (9 x 4) = 89'''


def produto_escalar(lista_x, lista_y):
    nova_lista = []
    for i in range(len(lista_x)):
        multi = lista_x[i] * lista_y[i]
        nova_lista.append(multi)
    return nova_lista

def soma_da_nova_lista(nova_lista):
    soma = sum(nova_lista)
    return soma

def main():
    lista_x = []
    lista_y = []
    for i in range(5):
        numerox = float(input())
        lista_x.append(int(numerox))
    for i in range(5):
        numeroy = float(input())
        lista_y.append(int(numeroy))
    
    nova_lista = produto_escalar(lista_x, lista_y)
    soma = soma_da_nova_lista(nova_lista)
    print(f'{lista_x}\n{lista_y}')
    print(f'({lista_x[0]} x {lista_y[0]}) + ({lista_x[1]} x {lista_y[1]}) + '
          f'({lista_x[2]} x {lista_y[2]}) + ({lista_x[3]} x {lista_y[3]}) + '
          f'({lista_x[4]} x {lista_y[4]}) = {soma}')    
if __name__ == '__main__':
    main()
        
        