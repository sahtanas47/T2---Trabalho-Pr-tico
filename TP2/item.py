class Item:
    def __init__(self, titulo, ano):
        self.titulo = titulo
        self.ano = ano
        self.disponivel = True

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            return True
        return False

    def exibir_detalhes(self):
        status = "Disponível" if self.disponivel else "Emprestado"
        return f"Título: {self.titulo} | Ano: {self.ano} | Status: {status}"