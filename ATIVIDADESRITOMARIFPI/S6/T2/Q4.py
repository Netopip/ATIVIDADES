def converter(idade_terrestre):
    idade_espacial = idade_terrestre // 2
    return idade_espacial

def main():
    idade_terrestre = int(input())

    idade_espacial = converter(idade_terrestre)

    print(idade_espacial)

if __name__ == "__main__":
    main()
