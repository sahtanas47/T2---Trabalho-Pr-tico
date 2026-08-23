from prateleira import Prateleira

class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.prateleiras = {}

    def criar_prateleira(self, ID):
        if ID not in self.prateleiras:
            nova_prateleira = Prateleira(ID)
            self.prateleiras[ID] = nova_prateleira
            return nova_prateleira
        return self.prateleiras[ID]

    def buscar_prateleira(self, ID):
        return self.prateleiras.get(ID)