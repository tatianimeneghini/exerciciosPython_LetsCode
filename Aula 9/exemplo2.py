class moto():
	numero_roda = 0
	freio = False
	motor = ""
	banco = False
	ignicao = ""
	velocidade = ""
	retrovisor = False

class cadeira():
	
	def __init__(numero_perna, material, tipo_encosto, cor, tamanho): 
	#função construtora. Sintaxe: def __init__(self, <atributo1>, <atributo2, ...):
	#O self amarra os parâmetros aos atributos dos objetos.
	numero_perna = 0
	material = ""
	tipo_encosto = ""
	cor = ""
	tamanho = ""

moto1 = moto()

moto1.numero_roda = 2
moto1.freio = True
moto1.motor = "elétrico"
moto1.banco = True
moto1.ignicao = "elétrico"
moto1.velocidade = "150 km"
moto1.retrovisor = True

cadeira_sala = cadeira()
cadeira_sala.numero_perna = 2
cadeira_sala.material = "madeira"
cadeira_sala.encosto = "pequeno"
cadeira_sala.cor = "amarelo"
cadeira_sala.tamanho = "tamanho médio"

print(moto1.velocidade)
print(cadeira_sala.material)