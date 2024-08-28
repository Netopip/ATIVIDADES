def main():
    cont_par = 0
    cont_impar = 0
    for i in range(100):
        numero = int(input())
        if numero % 2 == 0:
            cont_par += 1
        else:
            cont_impar += 1
    print(cont_par)
    print(cont_impar)
if __name__ == '__main__':
    main()