class Pessoa():
	def __init__(self, nome, estado_filial, idade):
		self.nome = nome
		self.estado_filial = estado_filial
		self.idade = idade

	def mostrar(self):
		print("O nome é ", nome)
		print("O estado é ", estado_filial)
		print("A idade é ", idade)

class Funcionario(Pessoa):
	def __init__(self, nome, estado_filial, idade, cargo):
		Pessoa.__init__(self, nome, estado_filial, idade)
		self.cargo = cargo
		self.tempo = tempo

class Cliente(Pessoa):
	def __init__(self, nome, estado_filial, idade):
		Pessoa.__init__(self, nome, estado_filial, idade)
		self.rg = rg