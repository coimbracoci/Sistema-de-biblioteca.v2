from livro import Livro
from usuario import Usuario
from emprestimo import Emprestimo

obj1 = Livro('A Senhora', 'Machado de Assis', 85)
obj2 = Usuario('Matheus', 2345)
obj3 = Emprestimo(obj2, obj1, 5)
print(obj3.realizar_emprestimo())
print(obj3.realizar_devolucao())
print(obj3.realizar_devolucao())
print(obj3.resumo())