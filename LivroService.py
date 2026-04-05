from livro import Livro
from rich.panel import Panel
from rich import print

class LivroService:

    ListaLivro = []

    @classmethod
    def adicionar(cls, livro):
        cls.ListaLivro.append(livro)
        print(f"Criado com sucesso")

    @classmethod
    def editar(cls, indice, novo_titulo, novo_autor):
        try:
            livro = cls.ListaLivro[indice]
            
            if novo_titulo:
                livro.titulo = novo_titulo

            if novo_autor:
                livro.autor = novo_autor

        except IndexError:
            print(f'Indice invalido')

    @classmethod
    def listar(cls):
            if not cls.ListaLivro:
                print("[red]Lista vazia[/red]")
                return
            
            for indice, valor in enumerate(cls.ListaLivro):
                print(f"[green]{indice} --- {valor}[/green]")
        
    @classmethod
    def excluir(cls, indice):
        if indice < 0:
            print(f"Posição de indice invalida.")
            return
        try:
            cls.ListaLivro.pop(indice)
        except IndexError:
            print(f"ERRO: indice invalido")