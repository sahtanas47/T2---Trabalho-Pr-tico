from item import Item

class HQ(Item):
    def __init__(self, titulo, ano, edicao):
        super().__init__(titulo, ano)
        self.edicao = edicao

    def exibir_detalhes(self):
        base = super().exibir_detalhes()
        return f"[HQ] {base} | Edição nº: {self.edicao}"
    