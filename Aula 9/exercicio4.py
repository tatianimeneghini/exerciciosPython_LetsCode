class Funcionario():
	def __init__(self, nome, funcao, salario): 
		self.nome = nome
		self.funcao = funcao
		self.salario = salario
	
Ana = Funcionario("Ana Pereira", "Diretora", 6000)
Mario = Funcionario("Mario Rossi", "Secretário", 4000)
Luana = Funcionario("Luana Barbosa", "Gerente", 3000)

def aumentar_salario(salario_antigo):
	print(salario_antigo+500)

aumentar_salario(Luana.salario)