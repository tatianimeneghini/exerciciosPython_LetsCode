def funcao(grupo):
	auxiliar = 0
	for i in grupo:
		if type(i) == type(int()) or type(i) == type(float()) or type(i) == type(str()):
		auxiliar += 1
		return True
		else:
			return False
	if auxiliar == len(grupo):
		posicao = 0
		for i in grupo:
			i = int(i)
			grupo[posicao] = i
			posicao += 1 

grupo = list(range(-25, 25))

f = (funcao(grupo))
print(funcao)