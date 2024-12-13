'''ME FAÇA UMA QUESTAO DE POO
Claro! Vamos a uma questão prática de Programação Orientada a Objetos (POO):

Questão:
Classe Biblioteca: Implemente uma classe Biblioteca que gerencia uma coleção de livros.

Um livro deve ser representado pela classe Livro e deve possuir os seguintes atributos:

título (string)

autor (string)

ano de publicação (inteiro)

A classe Biblioteca deve possuir os seguintes métodos:

adicionar_livro: Adiciona um novo livro à coleção da biblioteca.

remover_livro: Remove um livro da coleção com base no título.

buscar_livro: Retorna o livro com base no título.

listar_livros: Lista todos os livros na biblioteca.

livros_por_autor: Retorna uma lista de livros escritos por um autor específico.

Implemente também a classe Livro com um método para:

exibir_detalhes: Exibe os deta'''

class Bibliotecas:
    def __init__(self):
        self.livros = []

    def adicionarLivros(self,novo_livro):
        self.livros.append(novo_livro)
        return f'Livro {novo_livro.titulo_livro} adicionado a biblioteca'


    def removerLivro(self,titulo):
        for livro in self.livros:
            if livro.titulo_livro == titulo:
                self.livros.remove(livro)
                return f'Livro {titulo} removido da biblioteca.'
        return f'Livro {titulo} não encontrado'

    def buscarLivro(self,titulo):
        for livro in self.livros:
            if livro.titulo_livro == titulo:
                return f'{livro.exibirDetalheslivros()}'
        return f'Livro {titulo} não encontrado.'

    def listarLivro(self):
        if not self.livros:
            return f'Não há livros na biblioteca'
        detalhes_livros = '\n'.join([livro.exibirdetalhes() for livro in self.livros])
        return detalhes_livros


    def livrosporautor(self,autor):
        livros_autor = [livro.exibirdetalhes() for livro in self.livros if livro.autor == autor]
        if livros_autor:
            return '\n'.join(livros_autor)
        return f'Autor {autor} não encontrado.'

class Livro:
    def __init__(self,titulo_livro,autor='Desconhecido', data_publi=None):
        self.titulo_livro = titulo_livro
        self.autor = autor
        self.data_publi = data_publi

    def exibirdetalhes(self):
        return f'Titulo do livro: {self.titulo_livro}\nAutor: {self.autor}\nData da publicação: {self.data_publi}\n'



livro = Livro(titulo_livro='Dom casmurro',data_publi=2015)
livro2 = Livro('Dom quixote','Zé Cabral',2016)
livro3 = Livro('Zé da Burra','Zé Cabral',2019)
bibli = Bibliotecas()
bibli.adicionarLivros(livro)
bibli.adicionarLivros(livro2)
bibli.adicionarLivros(livro3)
print(bibli.listarLivro())
print()
print('Livros por autor')
print(bibli.livrosporautor('Zé Cabral'))
print(bibli.livrosporautor('Zé nojento'))
print()

print(bibli.removerLivro('Dom casmurro'))



