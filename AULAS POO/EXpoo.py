class Carro:
    def __init__(self,marca, modelo, cor , ano):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        
    
    
carro1 = Carro('Fiat', 'Argo', 'Azul', 2024)
print(f'O carro é um {carro1.marca}, {carro1.modelo} de cor {carro1.cor} do ano de {carro1.ano}.')
carro2 = Carro('Buggat','Chiron','Preto',2024)
print(carro2.modelo)
        
            