from livro import Livro
from rich.panel import Panel

class Biblioteca:
    
    def adicionar(self):
        Livro.ListaLivro.append({"Autor":self.autor, "Titulo":self.titulo, "Genero":self.genero, "Ano":self.ano})
        return self.ListaLivro

    def listar_livros(self):
        return f"{Panel(Livro.ListaLivro, title = "livros")}"

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
