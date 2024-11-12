from livros import livros
from config import Database

class ControllerLivro:
    def cadastrarlivro(self):
        bd = Database("localhost","root","","biblioteca")
        bd.conectar()

        livro = livros("Dom Casmurro","Machado de Assis","Suspense",123 )
        bd.cursor.execute(livro.create())
        bd.conexao.commit()
        bd.desconectar()

    def ProcurarLivro(self):
        
