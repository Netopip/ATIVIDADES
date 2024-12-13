class Banco:
    def __init__(self,nome_banco):
        self.nome_banco = nome_banco
        self.contas = []

    def adicionarconta(self,conta):
        self.contas.append(conta)

    def removerconta(self,numero_conta):
        for conta in self.contas:
            if conta.__numero_conta == numero_conta:
                self.contas.remove(conta)
                return f'Conta numero {conta.__numero_conta} do correntista {conta.__nome_correntista} removida com sucesso'
        return f'Conta {conta.__numero_conta} já removida ou não existente'

    def buscarconta(self,numero_conta):
        for conta in self.contas:
            if conta.__numero_conta == numero_conta:
                return f'{conta.exibircorrentista()}'
        return f'Correntista {numero_conta} não encontrado.'

    def exibircontasbanco(self):
        if not self.contas:
            return f'Não a contas cadastradas no {self.nome_banco}'
        detalhes_correntistas = '\n'.join([conta.exibircorrentista() for conta in self.contas])
        return detalhes_correntistas

    def saldototalbanco(self):
        saldo_total = 0
        for conta in self.contas:
            saldo_total += conta.__saldo
        return f'O saldo total do banco {self.nome_banco} é de R$ {saldo_total}'



class Contacorrente:
    def __init__(self,numero_conta,nome_correntista,saldo=float):
        self.__numero_conta = numero_conta
        self.__nome_correntista = nome_correntista
        self.__saldo = saldo

    @property
    def getnumeroconta(self):
        return self.__numero_conta
    @property
    def getnome(self):
        return self.__nome_correntista
    @property
    def getsaldo(self):
        return self.__saldo

    def depositar(self,valor):
        if valor < 0:
            return f'Não é possível adicionar esse valor.'
        self.__saldo += valor
        return f'Depósito do correntista {self.__nome_correntista} no valor de R$ {valor:.2f} bem sucedido.'


    def sacar(self,valor):
        if self.__saldo < valor:
            return f'Operação inválida, saldo insuficiente.'
        self.__saldo -= valor
        return f'Operação bem sucedida, saque de {valor}.'


    def exibircorrentista(self):
        return f'Nº conta: {self.__numero_conta}\nCorrentista: {self.__nome_correntista}\nSaldo: {self.__saldo}'


neto = Contacorrente(599-9,'Neto',1000)
print(neto.getnumeroconta)
print(neto.getsaldo)
