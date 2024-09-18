def ordem_crescente(num1, num2, num3):
    numeros_ordenados = sorted([num1, num2, num3])
    return numeros_ordenados

def main():
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())

    ordenados = ordem_crescente(num1, num2, num3)
    
    print(ordenados[0])
    print(ordenados[1])
    print(ordenados[2])

if __name__ == "__main__":
    main()
