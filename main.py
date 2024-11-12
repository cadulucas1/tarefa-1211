from livros import livros
from usuario import usuario
from biblioteca import biblioteca
from controllerlivro import ControllerLivro
import mysql.connector

conexao = mysql.connector.connect(
   host='10.28.2.66',
   user='suporte',
   password='suporte',
   database='biblioteca'
)
