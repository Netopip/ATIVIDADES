distancia = float(input())
velocidade = float(input())

tempo_em_horas = distancia / velocidade
dias = int(tempo_em_horas // 24)
horas_restantes = int(tempo_em_horas % 24)
 
print(dias,"dias e", horas_restantes,"horas")
