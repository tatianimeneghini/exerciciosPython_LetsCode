nome = str(input("Insira seu nome: "))
h = int(input("Insira o horário de agora (24 horas)"))

def horario (h, nome):
	if h > 0 and h < 12:
		print("Bom dia, ", nome)	
	elif h > 12 and h < 18:
		print("Boa tarde, ", nome)
	elif h > 18 and h < 24:
		print("Boa noite, ", nome)
	else:
		h = int(input("Informacao inválida. Insira o horário de agora (24 horas)"))

horario(h, nome)
