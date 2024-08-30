times =('Botafogo','Atlético-MG','Bragantino','Athletico-PR','Bahia','Internacional',	
        'Cruzeiro','Flamengo','Grêmio','Criciúma','Fortaleza','Palmeiras','Juventude',
        'São Paulo','Corinthians','Fluminense','Vasco da Gama','Vitória','Atlético','Cuiabá')

print(f'A lista de times do brasileirao: {times}')
print('-=' * 20)
print(f'Os 5 primeiros times são : {times[0:5]}')
print('-=' * 20)
print(f'Os 4 ultimos são: {times[-4:]} ')
print('-=' * 20)
print(f'Times em ordem alfabetica: {sorted(times)}')
print('-=' * 20)
print(f'O Flamengo está na {times.index("Flamengo")+ 1}° posição')
