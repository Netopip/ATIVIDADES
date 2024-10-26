class Relogio:
    def __init__(self, hora=0, minuto=0):
        self.hora = hora
        self.minuto = minuto

    def mudarHora(self, nova_hora):
        if nova_hora < 0 or nova_hora > 23:
            return 'Não é possível alterar, valor de hora inválido'
        else:
            self.hora = nova_hora

    def mudarMinuto(self, novo_minuto):
        if novo_minuto < 0 or novo_minuto > 59:
            return 'Não é possível alterar, valor de minuto inválido'
        else:
            self.minuto = novo_minuto

    def retornarHoras(self):
        return f'{self.hora:02d}:{self.minuto:02d}'


relogio = Relogio(5, 20)
print(relogio.retornarHoras())  
print(relogio.mudarHora(25))
print(relogio.retornarHoras())  
