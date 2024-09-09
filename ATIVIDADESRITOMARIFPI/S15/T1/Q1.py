'''01. Considereuma tupla que guarde temperaturas em Celsius (C) ou Fahrenheit (F) como um valor em duas partes:
temperatura e escala. Por exemplo: 32,5 graus Celsius é representado como (32.5, ‘C’) e 45,2 graus Fahrenheit é
representado como (45.2, ‘F’). Crie uma função que recebe duas temperaturas e retorna a mais alta. Caso as
temperaturas sejam de escalas diferentes, a função deve fazer a conversão antes de compará-las. Faça a leitura de
duas temperaturas, na forma temperatura e escala (t, e) separadamente, e mostre qual é a maior. Considere até 4
(quatro) casas decimais).
Use upper() e colchetes [] para garantir a leitura correta da escala com apenas um caractere, por exemplo:
escala = input('Escala : ').upper()[0]
As fórmulas, a seguir, mostram como realizar a conversão entre as escalas solicitadas::
°F = (°C * (9/5)) + 32 | °C = (°F - 32) * (5/9)'''


def main():
    t1 = ()
    t2 = ()
    temp1 = float(input())    
    
    
if __name__ == '__main__':
    main()