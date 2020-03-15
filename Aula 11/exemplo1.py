#Atributos são as variáveis. Métodos são as funções.

class Cachorro():
	def __init__(self, nome, raca, porte, dono):
		#Esses são os atributos do código.
		self.nome = nome
		self.raca = raca
		self.porte = porte
		self.dono = dono

	#Esses são os métodos.
	def latir(self):
		print("au au au") #<pass> não faz nada

	def correr(self):
		print(self.nome+" está correndo")

	def morder(self):
		print(self.nome+" está mordendo")

bilu = Cachorro("Bilu", "Yorkshire", "pequeno", "João")
print(bilu.nome)
bilu.latir()
bilu.correr()
bilu.morder()