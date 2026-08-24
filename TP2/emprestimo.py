from usuario import Usuario
from item import Item

class Emprestimo:
    def __init__(self, usuario, item):
        self.usuario = usuario
        self.item = item
        self.ativo = False

    def realizar_emprestimo(self):
        if self.item.emprestar():
            self.ativo = True
            return True
        return False

    def finalizar_emprestimo(self):
        if self.ativo:
            self.ativo = False
            print("Empréstimo Finalizado!")
        else:
            print("Esse empréstimo não existe!")

    def resumir(self):
        status = "Ativo" if self.ativo else "Finalizado"
        return f"Usuário: {self.usuario.nome} | Item: {self.item.titulo} | Status: {status}"
