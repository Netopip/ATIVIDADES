
def par_impar(x):
    if x % 2 == 0:
        return False
    elif x % 2 != 0:
        return True

def main():
    numero = int(input())
    print(f"{par_impar(numero)}")
if __name__== "__main__":
    main()
