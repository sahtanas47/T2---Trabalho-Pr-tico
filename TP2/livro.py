from item import Item

class Livro(Item):
    def __init__(self, titulo, ano, autor, num_paginas):
        super().__init__(titulo, ano)
        self.autor = autor
        self.num_paginas = num_paginas
        
    def exibir_detalhes(self):
        base = super().exibir_detalhes()
        return f"[TIPO: LIVRO]{base} | Autor: {self.autor} | Páginas: {self.num_paginas}"
