'''ME FAÇA UMA QUESTOES DE POO
Claro! Aqui vai uma questão para você praticar Programação Orientada a Objetos (POO):

Questão:
Classe Banco: Implemente uma classe Banco que simula o funcionamento de um banco. Um banco deve possuir um nome (string) e uma lista de contas correntes.

Cada conta corrente deve ser representada pela classe ContaCorrente e possuir os seguintes atributos:

número da conta (inteiro)

nome do correntista (string)

saldo (float)

A classe Banco deve possuir os seguintes métodos:

adicionar_conta: Adiciona uma nova conta corrente à lista de contas do banco.

remover_conta: Remove uma conta corrente da lista com base no número da conta.

buscar_conta: Retorna a conta corrente com base no número da conta.

total_saldo: Retorna o saldo total de todas as contas correntes no banco.

Implemente também a classe ContaCorrente com métodos para:

depositar: Adiciona um valor ao saldo da conta corrente.

sacar: Subtrai um valor do saldo da conta corrente, caso haja saldo suficiente.

Exemplo de Uso:
Crie um banco chamado "Banco do Brasil".

Adicione duas contas correntes ao banco.

Realize operações de depósito e saque nas contas.

Busque uma conta pelo número da conta e exiba os detalhes.

Exiba o saldo total de todas as contas no banco.

Vamos ver como você se sai com essa tarefa de POO!

Se precisar de ajuda, estou aqui para isso! '''


class Banco:
    def __init__(self,nome_banco):
        self.nome_banco = nome_banco
        self.contas = []
    
    def adicionarconta(self,conta):
        self.contas.append(conta)
        
    def removerconta(self,numero_conta):
        for conta in self.contas:
            if conta.numero_conta == numero_conta:
                self.contas.remove(conta)
                return f'Conta numero {conta.numero_conta} do correntista {conta.nome_correntista} removida com sucesso'
        return f'Conta {conta.numero_conta} já removida ou não existente'
    
    def buscarconta(self,nome_correntista):
        for conta in self.contas:
            if conta.nome_correntista == nome_correntista:
                return f'{conta.exibircorrentista()}'
        return f'Correntista {nome_correntista} não encontrado.'
    
    def exibircontasbanco(self):
        if not self.contas:
            return f'Não a contas cadastradas no {self.nome_banco}'
        detalhes_correntistas = '\n'.join([conta.exibircorrentista() for conta in self.contas])
        return detalhes_correntistas
    
    def saldototalbanco(self):
        saldo_total = 0
        for conta in self.contas:
            saldo_total += conta.saldo
        return f'O saldo total do banco {self.nome_banco} é de R$ {saldo_total}'
            
    

class Contacorrente:
    def __init__(self,numero_conta,nome_correntista,saldo=float):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo
        
    def depositar(self,valor):
        if valor < 0:
            return f'Não é possível adicionar esse valor.'
        self.saldo += valor
        return f'Depósito do correntista {self.nome_correntista} no valor de R$ {valor:.2f} bem sucedido.'
        
    
    def sacar(self,valor):
        if self.saldo < valor:
            return f'Operação inválida, saldo insuficiente.'
        return f'Operação bem sucedida, saque de {valor}.'
    
    def exibircorrentista(self):
        return f'Nº conta: {self.numero_conta}\nCorrentista: {self.nome_correntista}\nSaldo: {self.saldo}'
    

banco = Banco('Banco de Brasil')
cliente1 = Contacorrente(numero_conta='556-43',nome_correntista='Neto',saldo=0)
cliente2 = Contacorrente('586-22', 'Valdir', 1632.45)

banco.adicionarconta(cliente1)
banco.adicionarconta(cliente2)


print(banco.exibircontasbanco())
print(banco.saldototalbanco())


banco2 = Banco('Caixa')
cliente_a = Contacorrente('545-45','Neto',1340)
cliente_b = Contacorrente('545-46','Jonas',1000)

banco2.adicionarconta(cliente_a)
banco2.adicionarconta(cliente_b)

print(banco2.saldototalbanco())
print(cliente_b.depositar(500))
print(banco2.saldototalbanco())
print(banco2.exibircontasbanco())
print()
print('Buscar conta:')
print(banco2.buscarconta('jona'))