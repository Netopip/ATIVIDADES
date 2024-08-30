def calcular_area(lado):
    area = lado ** 2
    return area

def main():
    lado = int(input('digite um munero do lado'))
    
    area_total = calcular_area(lado)
    print(f'A area total da figura é {area_total} metros quadrados')

if __name__ == "__main__":
    main()