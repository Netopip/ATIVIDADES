import math

def calcular_sen_cos_tg(angulo):
    seno = math.sin(math.radians(angulo))
    cosseno = math.cos(math.radians(angulo))
    tangente = math.tan(math.radians(angulo)) #O .radians() é o foramto em que se le o angulo (radianos)
    return seno, cosseno, tangente
            
def main():
    angulo = int(input('Digite o angulo:'))

    seno, cosseno, tangente = calcular_sen_cos_tg(angulo)

    print(f'O seno de {angulo} é {seno:.2f}')
    print(f'O cosseno de {angulo} é {cosseno:.2f}')
    print(f'A tangente de {angulo} é {tangente:.2f}')

if __name__ == "__main__":
    main()
