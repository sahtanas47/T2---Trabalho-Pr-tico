from usuario import Usuario
from item import Item
from datetime import date

class Emprestimo:
    def __init__(self, usuario, item):
        self.usuario = usuario
        self.item = item
        self.data_emprestimo = date.today()
        self.ativo = False

    def realizar_emprestimo(self):
        if self.item.emprestar():
            self.ativo = True
            self.data_emprestimo = date.today()
            return True
        return False

    def finalizar_emprestimo(self):
        if self.ativo:
            self.item.devolver()
            self.ativo = False

    def resumir(self) -> str:
        status = "Ativo" if self.ativo else "Finalizado"
        data_pt = self.data_emprestimo.strftime("%d/%m/%Y")
        return f"Usuário: {self.usuario.nome} | Item: {self.item.titulo} | Data: {data_pt} | Status: {status}"