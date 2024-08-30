def calcualar_h(n):
    h = [1]
    for i in range(2,n+1):
        prt = 1 / i
        h.append(prt)
    return sum(h)


def main():
    numero = int(input())
    msg = calcualar_h(numero)
    print(f'{msg:.4f}')

if __name__ =='__main__':
    main()

