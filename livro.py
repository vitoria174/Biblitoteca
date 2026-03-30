class Livro:
    def __init__(self, titulo, autor, ano, genero, quant_disponivel = 0, disponivel = False):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.genero = genero
        self.quant_disponivel = quant_disponivel
        self.disponivel = disponivel

    def __str__(self):
        return f"O livro {self.titulo} escrito por {self.autor}, no ano {self.ano} do genero {self.genero} tem quant {self.quant_disponivel}"
    


l1 = Livro('o alquimista','Paulo coelho','2001','fantasia',5)
print(l1)

