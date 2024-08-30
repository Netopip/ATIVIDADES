def main():
    x = int(input())#20
    y = int(input())#100
    div = 0
    for i in range(x, y + 1):# intervalo de 20 ate o 101.
        for n in range(1, i+1):# o intervalo sera de 1 ate o iteravel da vez que no caso é 20(que nao e primo)
            if i % n == 0:# se nesse intervalo a divisao de 20 pelos numeros de 1 a 20 passar de dois é pq ele nao e primo.
                div += 1
        if div == 2:
            print(f'{i}')
        div = 0

if __name__ == '__main__':
    main()