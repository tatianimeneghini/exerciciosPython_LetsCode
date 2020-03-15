#Polimorfismo é um método herdado mas que se comporta de modo diferente.
#É possível generalizar também os métodos, além dos atributos.
class Pet(): #super-classe
	def __init__(self, nome, raca, dono):
		self.nome = nome
		self.raca = raca
		self.dono = dono

	def correr(self): #Generalizar os métodos.
		pass #As duas classes correm de maneiras diferentes.

	def morder(self):
		pass

	def pular(self):
		pass

class Cachorro(Pet): #subclasse.
	def __init__(self, nome, raca, dono, porte):
		Pet.__init__(self, nome, raca, dono):
		self.porte = porte

	def latir(self):
		print("au au au")

	def correr(self):
		print(self.nome+" corre rápido")

	def morder(self):
		print(self.nome+" morde mais forte")

	def pular(self):
		print(self.nome+" pula mais alto")

class Gato(Pet): #subclasse
	def __init__(self, nome, raca, dono):
		Pet.__init__(self, nome, raca, dono):
		pass

	def miar(self):
		print("miau miau")

	def ronronar(self):
		print(self.nome+" está ronronando no edredom")

			def correr(self):
		print(self.nome+" corre devagar")

	def morder(self):
		print(self.nome+" morde suave")

	def pular(self):
		print(self.nome+" pula menos alto")