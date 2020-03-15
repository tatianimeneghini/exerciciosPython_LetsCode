import os #Manipula arquivos, pastas do Sistema Operacional (SO).
import matplotlib.pyplot as plt #Biblioteca do Python que gera gráficos. 
#O "as" siginifica "como", que significa que o tipo de arquivo pode ser chamado como uma palavra menor, como um apelido.
import collections #Biblioteca de Python Collections.

class Funcionarios():
	def __init__(self, codigo, nome, idade, cargo, salario, estado_filial):
		self.codigo = codigo
		self.nome = nome
		self.idade = idade
		self.cargo = cargo
		self.salario = salario
		self.estado_filial = estado_filial

def incluir(codigo):
	nome = input("Digite o nome: ")

	idade = int(input("Digite a idade: "))
	while idade <18 or idade > 65:
		print("Idade inválida.")
		idade = int(input("Digite a idade: "))

	cargo = int(input("Qual o cargo? 1 - Gerente, 2 - Vendedor, 3 - Repositor, 4 - Limpeza "))
	while cargo < 1 or cargo > 4:
		print("Código de cargo inválido.")
		cargo = int(input("Qual o cargo? 1 - Gerente, 2 - Vendedor, 3 - Repositor, 4 - Limpeza "))

	salario = float(input("Digite o salário: "))
	while salario < 0:
		print("Salário inválido. Somente positivo. ")
		salario = float(input("Digite o salário: "))

	estado_filial = input("Digite a sigla do estado da filial: ")

	func = Funcionarios(codigo, nome, idade, cargo, salario, estado_filial)

	print(func.nome, func.idade, func.salario, func.estado_filial)

	file = open('banco_de_dados.csv', 'a')
	file.write(str(func.codigo)+'|'+func.nome+'|'+str(func.idade)
		+'|'+str(func.cargo)+'|'+str(func.salario)+'|'+func.estado_filial+'\n') 
#A barra "|" é mais recomendável para quebrar a linha do código.
#A barra n "\n" quebra linha na execução do código.

file = open('registros.csv', 'r')
conteudo = file.readlines()

lista_filiais = []
for registro in conteudo: #Para percorrer todos os registros do arquivo.
	filial = registro.split('|')[-1] #Criar uma lista para não perder as informações e poder analisar depois.
	lista_filiais.append(filial[:2]) #Ignorar o \n

result = collections.Counter(lista_filiais)

print(result.keys())
print(result.values())

plt.bar(result.keys(), result.values())
plt.ylabel("Número de funcionários")
plt.xlabel("Estados")
plt.title("Quantidade de funcionários por Estado")
plt.show()

#plt.plot(list(range(100))) #Executa um gráfico.
#plt.show()

"""if os.path.isfile('banco_de_dados.csv'): #Se esse arquivo for verdadeiro, abrir no arquivo
	file = open('banco_de_dados.csv', 'r')
	conteudo = file.readlines() #Ler linha do dicionário.
	codigo = int(conteudo[-1].split('|')[0]) #Mostrar as últimas informações inseridas. 
#O split separa os elementos a partir de um separador definido e transforma em lista. Sintaxe: <split()>
else:
codigo = 0

control = 1 #Variável para o usuário cadastrar funcionários novos.
while control != 2:
	codigo += 1
	incluir(codigo)
	control = int(input("Deseja cadastrar outro funcionário? 1 - Sim, 2 - Não ")) """