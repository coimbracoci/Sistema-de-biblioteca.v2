class Emprestimo:
    def __init__(self, usuario, livro, dias_emprestimo):
        self.usuario = usuario
        self.livro = livro
        self.dias_emprestimo = dias_emprestimo

    def realizar_emprestimo(self):
        if self.dias_emprestimo > 0:
            if self.livro.disponivel == True:
                self.livro.disponivel = False
                return f"Empréstimo realizado com sucesso! Aproveite."
            else:
                return f"Infelizmente o livro não está disponível. Tente outro livro em nosso portal."
        else:
            return f"Empréstimo inválido, tente outro dia."
    
    def realizar_devolucao(self):
        if self.livro.disponivel == False:
            self.livro.disponivel = True
            return f"Livro devolvido com sucesso! Aproveite nosso catálogo."
        else:
            return f"Não há emprestimo ativo no momento."
    def resumo(self):
        return f"Nome: {self.usuario.nome_usuario} \n Livro: {self.livro.titulo_livro} \n Dias de empréstimo: {self.dias_emprestimo}"