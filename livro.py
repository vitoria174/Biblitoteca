class Livro:
    def __init__(self, titulo:str, autor:str, ano:int, genero:str, quant_disponivel:int):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.genero = genero

        if quant_disponivel < 0:
            raise ValueError("Quantidade invalida")
        self.quantidade = quant_disponivel

    def disponivel(self):
        return self.quantidade > 0

    def __str__(self):
        status = "Disponivel" if self.quantidade else "Indisponivel"
        return (
            f"Titulo {self.titulo} | Autor: {self.autor} | Ano: {self.ano} | Genero: {self.genero} | Quant: {self.quantidade} | Status: {status}"
        )
    
    
        
