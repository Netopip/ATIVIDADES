def calcular_reajuste(salario):
    reajuste = salario + (salario * (15/100))
    return reajuste

def main():
    salario = float(input("qual o salario: R$"))

    novo_salario = calcular_reajuste(salario)

    print(f'O novo salario com aumento será de R$ {novo_salario}')

if __name__ == "__main__":
    main()