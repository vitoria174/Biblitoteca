from LivroService import LivroService
from livro import Livro
from rich import print
from rich.panel import Panel

def criar():
    try:
        titulo = str(input("Titulo: "))
        autor = str(input("Autor: "))
        ano = int(input("Ano: "))
        genero = str(input("Genero: "))
        quantidade = int(input("Quantidade: "))
        livro = Livro(titulo, autor, ano, genero, quantidade)
        LivroService.adicionar(livro)
    except:
        print("comando não identificado")

def editar():
    LivroService.listar()
    try:
        indice = int(input("Digite o indice: "))
        novo_titulo = str(input("Novo titulo: "))
        novo_autor = str(input("Novo autor: "))

        LivroService.editar(indice, novo_titulo, novo_autor)
    except:
        print("Condição invalida")

def ler():
    LivroService.listar()

def excluir():
        LivroService.listar()

        indice = int(input("Indice: "))

        resposta = str(input("Deseja excluir livro? [S/N]")).upper()[0]

        if resposta == "S":
            LivroService.excluir(indice)
        else:
           print("Sessão encerrada")

def main():
    

    while True:
        print("1 - Criar Livro")
        print("2 - Editar Livro")
        print("3 - Ler Livros")
        print("4 - Excluir Livro")
        print("0 - Sair")

        try:
            opcao = int(input("Digite opção: "))

            if opcao == 1:
                criar()
                
            elif opcao == 2:
                editar()

            elif opcao == 3:
                ler()
            
            elif opcao == 4:
                excluir()

            elif opcao == 0:
                break
        except IndexError:
            print("Comando invalido")

if __name__ == "__main__":
    main()