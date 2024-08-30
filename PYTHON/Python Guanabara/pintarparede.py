def calcular_tinta(lar, alt):
    area_parede = lar * alt
    litros_tinta = area_parede / 2
    return litros_tinta

def main():
    lar = float(input('Digite a largura da parede:'))
    alt = float(input('Digite a altura:'))

    litros_necessarios = calcular_tinta(lar, alt)
    
    print(f'Para pintar {lar * alt}m² será necessário {litros_necessarios}litros')

if __name__ == "__main__":
    main()



