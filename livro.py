class Livro:
    ListaLivro = []

    def __init__(self, autor, titulo,genero, ano):
        self.autor = autor
        self.titulo = titulo
        self.genero = genero
        self.ano = ano
        

    def __str__(self):
        return f"Autor {self.autor}, Titulo {self.titulo} Genero {self.genero} Ano {self.ano}"

    def adicionar(self):
        Livro.ListaLivro.append({"Nome":self.autor, "Titulo":self.titulo, "Genero":self.genero, "Ano":self.ano})
        return self.ListaLivro

    def listar_livros(self):
        for livros in self.ListaLivro:
            print(livros)

    def editar(self):
        pass


l1 = Livro('vito','amor','romance','2004')
l1.adicionar()
l2 = Livro('vivia','biomedica','romance','2006')
l2.adicionar()
l2.listar_livros()