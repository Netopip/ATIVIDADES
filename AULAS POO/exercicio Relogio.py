""


class Relogio:
    def __init__(self, hora, minuto):
        self.hora = hora
        self.minuto = minuto

    def alterarHora(self, nova_hora):
        if nova_hora < 0 or nova_hora > 23:
            return 'Não é possivel alterar o horário'
        else:
            self.hora = nova_hora
            return self.hora

    def alterarMinuto(self, novo_minuto):
        if novo_minuto < 0 or novo_minuto > 59:
            return 'Não é possivel aterar o horário'
        else:
            self.minuto = novo_minuto
            return self.minuto

    def retornarHorario(self):
        return f'{self.hora:02d}:{self.minuto:02d}'


relogio1 = Relogio(5, 20)
print(relogio1.retornarHorario())
relogio1.alterarHora(19)
relogio1.alterarMinuto(1)
print(relogio1.retornarHorario())
