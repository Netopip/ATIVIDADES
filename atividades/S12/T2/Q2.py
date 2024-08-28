def calcular_sequencia(n):
    if n < 2:
        return ''
    elif n >= 2:
        sequencia = [0,1]
        for i in range(2,n):
            pt = sequencia[-1] + sequencia[-2]
            sequencia.append(pt)
        return sequencia

def main():
    numero = int(input())
    resultado = calcular_sequencia(numero)
    print(*resultado, sep=', ')
if __name__ == '__main__':
    main()