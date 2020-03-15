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
	def __init__(self, nome, estado_filial, idade, cargo):
		Pessoa.__init__(self, nome, estado_filial, idade)
		self.cargo = cargo

class Gerente(Funcionario):
	def __init__(self, nome, estado_filial, idade, cargo, tempo_meses):
		Funcionario.__init__(self, nome, estado_filial, idade, cargo)
		self.tempo_meses = tempo_meses

lucas = Gerente("Lucas", "SP", 36, "Gerente", 15)
print("É "+lucas.cargo)
lucas.mostrar()