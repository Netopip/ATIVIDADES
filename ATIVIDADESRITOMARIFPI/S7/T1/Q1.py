def main():
    nome = input()
    sexo = int(input())

    if sexo == 1:
        print("Ilmo Sr.", nome)
    elif sexo == 2:
        print("Ilma Sra.", nome)
    else:
        print("Sexo invalido")

if __name__ == "__main__":
    main()
