nome = str(input("Insira seu nome: "))
idade = int(input("Digite sua idade: "))
provas = int(input("Quantas provas você fez? "))

if provas < 2:
	print("O número de provas tem que ser maior que dois.")
	provas = int(input("Quantas provas você fez? "))

nota = []
soma = 0
lista = []

for item in lista(0, provas):
	nota = float(input("Insira sua nota: "))

nota.remove(max(nota))
nota.remove(min(nota))

for item in nota:
	soma += item

media = soma/(provas - 2)

lista(nome)
lista(idade)
lista(provas)
lista(media)

if media > 5:
	lista(True)
else:
	lista(False)

print(lista)