from item import Item

class Prateleira:
    def __init__(self, ID):
        self.ID = ID
        self.itens = []

    def adicionar_item(self, item):
        self.itens.append(item)

    def listar_itens(self):
            for item in self.itens:
                print(f"  - {item.exibir_detalhes()}")
