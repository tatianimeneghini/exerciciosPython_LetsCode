class Pessoa():
	def __init__(self, nome, estado_filial, idade):
		self.nome = nome
		self.estado_filial = estado_filial
		self.idade = idade

	def mostrar(self):
		print("O nome é ", self.nome)
		print("O estado é ", self.estado_filial)
		print("A idade é ", self.idade)

class Funcionario(Pessoa):
	def __init__(self, nome, estado_filial, idade, cargo, salario):
		Pessoa.__init__(self, nome, estado_filial, idade, salario)
		self.cargo = cargo
		self.salario = salario

class Gerente(Funcionario):
	def __init__(self, nome, estado_filial, idade, cargo, salario):
		Funcionario.__init__(self, nome, estado_filial, idade, cargo, salario)

		def aumentar_salario(self):
			print("Seu salário aumentou! :D")

lucas = Gerente("Lucas", "SP", 36, "Gerente", 2.300)
fred = Funcionario("Fred", "AC", 56, "Operador de caixa", 1.400)

lucas.mostrar()
fred.mostrar()

lucas.aumentar_salario()
fred.aumentar_salario()