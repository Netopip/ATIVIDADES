def calcular_dia(dias):
    custo_dia = dias * 60
    return custo_dia

def calcular_km(km):
    custo_km = km * 0.15
    return custo_km

def main():
    dias = int(input('quantos dias alugados:')) 
    km = float(input('Quantos km rodados:'))

    total =calcular_dia(dias) + calcular_km(km)

    print(f'O total a pagar é de R$ {total:.2f}')

if __name__ == "__main__":
    main()

