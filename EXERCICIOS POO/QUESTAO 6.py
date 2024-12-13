'''QUESTAO PARA ADICIONAR E REMOVER ANIMAIS EM UM ZOOLOGIOC'''


class Zoologico:
    def __init__(self,nome_zoo):
        self.nome = nome_zoo
        self.animais = []

    def adicionaranimal(self,animal):
        self.animais.append(animal)
        return f'{animal.animal} colocado no {self.nome}'

    def removeranimal(self,nome_animal):
        for bicho in self.animais:
            if bicho.animal == nome_animal:
                self.animais.remove(nome_animal)
                return f'{nome_animal} retirado do {self.nome}'
        return f'Animal não existente no Zoo'

    def animaisdozoo(self):
        listar_animais = '\n'.join([animal.exibirdetalhes() + f'\nZoo:{self.nome}\n' for animal in self.animais])
        return listar_animais


class Animais:
    def __init__(self,animal,especie,peso):
        self.animal = animal
        self.especie =especie
        self.peso = peso

    def exibirdetalhes(self):
        return f'Animal: {self.animal}\nEspecie: {self.especie}\nPeso: {self.peso}kg'

zoobotanico = Zoologico('Zoobotanico')
parque = Zoologico('Parque')
macaco = Animais('Macaco','Chimpanzé',25)
leao = Animais('Leão','jubo',105)
onca = Animais('Onça','Pintada',145.5)
papagaio = Animais('Papagaio','Pássaro',1)

print(zoobotanico.adicionaranimal(macaco))
print(zoobotanico.adicionaranimal(leao))
print(zoobotanico.adicionaranimal(onca))
print(parque.adicionaranimal(papagaio))
print()
print(zoobotanico.animaisdozoo())
print(parque.animaisdozoo())


