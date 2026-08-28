from item import Item

class HQ(Item):
    def __init__(self, titulo, ano, edicao, autor):
        super().__init__(titulo, ano)
        self.edicao = edicao
        self.autor = autor

    def exibir_detalhes(self):
        base = super().exibir_detalhes()
        return f"[TIPO: HQ] {base} | Edição nº: {self.edicao} | Autor: {self.autor}"
    
