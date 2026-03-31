from livro import Livro

class LivroService:
    lista_Livro = []

    @classmethod
    def adicionar(cls, livro):
        cls.lista_Livro.append(livro)

    @classmethod
    def imprimir(cls):
        for indice, informacao in enumerate(cls.lista_Livro):
            print(f"{indice} - {informacao}")

    @classmethod
    def editar_livros(cls, indice, novo_titulo = None, novo_autor = None):
        try:
            livro = cls.lista_Livro[indice]

            if novo_titulo:
                livro.titulo = novo_titulo

            if novo_autor:
                livro.autor = novo_autor
        
        except:
            print("indice invalido")
    
    @classmethod
    def total_livros(cls):
        print(len(cls.lista_Livro))


