velocidade = float(input())
multa = (velocidade - 80) * 7
if velocidade <= 80:
    print(f'Siga tranquilo a essa velocidade!')
else:
    print(f'Voce foi multado em R${multa}')