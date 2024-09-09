'''Faça um programa que leia o tempo de duração de um evento em uma fábrica expresso em segundos. Calcule e exiba esse tempo em horas, minutos e segundos (HH:MM:SS).'''
def calcular_segundos(tempo):
    horas = int(tempo) // 3600
    minutos = (int(tempo) % 3600)//60
    segundos = int(tempo) % 60
    return horas,minutos,segundos

def main():
    tempo = str(input().strip())
    if tempo == '':
        print('00:00:00')
    else:
        horas,minutos,segundos = calcular_segundos(tempo)
        print(f'{horas:02}:{minutos:02}:{segundos:02}')
    
if __name__ == '__main__':
    main()
    