'''Classe Restaurante: Implemente uma classe Restaurante que gerencie o funcionamento de um restaurante.

Um restaurante deve possuir os seguintes atributos:

nome (string)

cardápio (dicionário com o nome do prato como chave e o preço como valor)

pedidos (lista de pedidos)

Cada pedido deve ser representado pela classe Pedido e deve possuir os seguintes atributos:

nome do cliente (string)

itens (dicionário com o nome do prato como chave e a quantidade como valor)

A classe Restaurante deve possuir os seguintes métodos:

adicionar_prato: Adiciona um novo prato ao cardápio.

remover_prato: Remove um prato do cardápio pelo nome.

fazer_pedido: Adiciona um novo pedido à lista de pedidos.

listar_pedidos: Lista todos os pedidos realizados, incluindo o nome do cliente e os itens pedidos.

calcular_total_pedido: Calcula o total de um pedido específico pelo nome do cliente.

calcular_total_dia: Calcula o total arrecadado no dia com todos os pedidos.

Implemente também a classe Pedido com métodos para:

adicionar_item: Adiciona um item ao pedido.

remover_item: Remove um item do pedido pelo nome.'''


class Restaurante:
    def __init__(self,nome):
        self.nome = nome
        self.cardapio = {}
        self.pedidos = []

    def adicionar_prato(self):
        pass

    def remover_prato(self):
        pass

    def fazer_pedido(self):
        pass

    def listar_pedidos(self):
        pass

    def calcular_total_pedido(self):
        pass

    def calcular_total_dia(self):
        pass


class Pedido:
    def __init__(self,nome_cliente):
        self.nome_clientes = nome_cliente
        self.itens = {}

    def adicionar_item(self):
        pass


    def remover_item(self):
        pass

