def sucessor(n1):
    suc = n1 + 1
    return suc
def antecessor(n1):
    ant = n1 - 1
    return ant
   
def main():
    n1 = int(input('Digite um numero:'))

    verificar = (f'O sucessor de {n1} é {sucessor(n1)}, e o antecessor de {n1} é {antecessor(n1)}')  

    print(verificar)

if __name__ == "__main__":
    main()