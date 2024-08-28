def main():
    maior = 0
    for i in range(100):
        numero = int(input())
        if numero > maior:
            maior = numero
    print(maior)
if __name__ == '__main__':
    main()
