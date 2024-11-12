class usuario:
    MAX_EMPRESTIMO = 3
    def __init__(self, nome, cpf, telefone):  
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.lista_livros = []

    def pegar_emprestado(self, livro):
        if len(self.lista_livros)== self.MAX_EMPRESTIMO:
            return
        
        self.usuario = usuario
        self.status = 'emprestado'

    def devolver_livro(self):
        if self.status != 'emprestado':
            return 'Não pode ser devolvido'
        