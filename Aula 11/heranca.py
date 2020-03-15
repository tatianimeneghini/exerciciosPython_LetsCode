#Herança é uma espécie de classe-mãe, com a generalização dos atributos.
class Pet(): #super-classe
	def __init__(self, nome, raca, dono):
		self.nome = nome
		self.raca = raca
		self.dono = dono

class Cachorro(Pet): #subclasse. Indica pro Python que essa classe é uma subclasse da super-classe pet.
	def __init__(self, nome, raca, dono, porte): #O cachorro herda os atributos da super-classe.
		Pet.__init__(self, nome, raca, dono): #Inicializa os atributos herdados.
		self.porte = porte

	def latir(self):
		print("au au au")

	def correr(self):
		print(self.nome+" está correndo")

	def morder(self):
		print(self.nome+" está mordendo")

class Gato(Pet): #subclasse
	def __init__(self, nome, raca, dono):
		Pet.__init__(self, nome, raca, dono):
		pass

	def pular(self):
		print(self.nome+" está pulando na cama")

	def miar(self):
		print("miau miau")

	def ronronar(self):
		print(self.nome+" está ronronando no edredom")