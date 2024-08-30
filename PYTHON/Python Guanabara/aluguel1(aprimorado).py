def calcular_aluguel(dias, km):
    custo_dia = dias * 60
    custo_km = km * 0.15
    custo_total = (custo_dia) + (custo_km)
    return custo_total

def main():
    dias = int(input('quantos dias alugados:')) 
    km = float(input('Quantos km rodados:'))

    total = calcular_aluguel(dias, km)

    print(f'O total a pagar é de R$ {total:.2f}')

if __name__ == "__main__":
    main()

