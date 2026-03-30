from livro import Livro

class LivroService:
    lista_Livro = []

    @classmethod
    def adicionar(cls, Livro):
        cls.lista_Livro.append(Livro)

    @classmethod
    def total_livros(cls):
        print(len(cls.lista_Livro))


l1 = Livro('a','b','c','d',1)
LivroService.adicionar(l1)
l2 = Livro('vida','vitoria','2001','romance',4)
LivroService.adicionar(l2)
LivroService.total_livros()