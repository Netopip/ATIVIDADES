class Bicicleta:
    def __init__(self,velocidade_atual=0,altura_cela=0,calibragem_pneu=0):
        self.velocidade_atual = velocidade_atual
        self.altura_cela = altura_cela
        self.calibragem_pneu = calibragem_pneu

    def aumentarCela(self,valor):
        if self.velocidade_atual != 0:
            return 'Não é possível aumentar a cela em movimento'
        else:
            nova_altura = self.altura_cela + valor
            if nova_altura > 15:
                return 'Não é possível aumentar cela para mais de 15cm'
            else:
                self.altura_cela = nova_altura
                return f'Altura da cela ajustada para {self.altura_cela}cm'


    def diminuirCela(self,valor):
        if self.velocidade_atual != 0:
            return 'Não é possível diminuir a cela em movimento'
        else:
            nova_altura = self.altura_cela - valor
            if nova_altura < 0:
                return 'Não é possível diminuti a cela para menos de 0cm'
            else:
                self.altura_cela = nova_altura
                return f'Altura da cela ajustada para {self.altura_cela}cm'

    def aumentarcalibrapneus(self,valor):
        if self.velocidade_atual != 0:
            return 'Não é possível calibrar pneus em movimento'
        else:
            calibragem = self.calibragem_pneu + valor
            if calibragem > 50:
                return 'Não é possível aumentar a calibragem para mais de 50'
            else:
                self.calibragem_pneu = calibragem
                return f'Calibragem de pneus ajustada para {self.calibragem_pneu}'


    def diminuircalibragempneus(self,valor):
        if self.velocidade_atual != 0:
            return 'Não é possível calibrar pneus em movimento'
        else:
            calibragem = self.calibragem_pneu - valor
            if calibragem < 0:
                return 'Não é possível diminuri a calibragem para menos de 0cm'
            else:
                self.calibragem_pneu = calibragem
                return f'Calibragem ajustada para {self.calibragem_pneu}'


bike = Bicicleta(20,0,25)
bike.velocidade_atual = 0
bike.aumentarCela(15)
print(bike.altura_cela)
print(bike.diminuirCela(1))
print(bike.aumentarcalibrapneus(25))
print((bike.diminuircalibragempneus(20)))