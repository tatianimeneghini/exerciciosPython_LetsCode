#Uma boa prática de programação, sempre divide em: MVC (Model, View, Control).

#Aqui é o Model:
class Cachorro():
	def __init__(self, nome, raca, porte, dono):
		#Esses são os atributos do código.
		self.nome = nome
		self.raca = raca
		self.porte = porte
		self.dono = dono

	def latir(self):
		print("au au au")

	def correr(self):
		print(self.nome+" está correndo")

	def morder(self):
		print(self.nome+" está mordendo")

class Gato():
	def __init__(self, nome, raca, dono):
		self.nome = nome
		self.raca = raca
		self.dono = dono

	def pular(self): #Os métodos são colocados, geralmente, depois ou em arquivos separado.
		print(self.nome+" está pulando na cama")

	def miar(self):
		print("miau miau")

	def ronronar(self):
		print(self.nome+" está ronronando no edredom")