from rich import print
from rich.panel import Panel

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
        Livro.ListaLivro.append({"Autor":self.autor, "Titulo":self.titulo, "Genero":self.genero, "Ano":self.ano})
        return self.ListaLivro

    def listar_livros(self):
        livros = [livro for livro in Livro.ListaLivro]
        print(Panel(str(livros), title= "Livros"))

    def editar(self, livro):

        encontrado = False

        for i in Livro.ListaLivro:
            if i["Autor"] == livro:
                i["Autor"] = "O alquimista"
                print("Editado")
                encontrado = True
                break
        if not encontrado:
                print('Não encontrado')


l1 = Livro('vito','amor','romance','2004')
l1.adicionar()
l2 = Livro('vivia','biomedica','romance','2006')
l2.adicionar()
l1.editar('vito')
l1.listar_livros()
