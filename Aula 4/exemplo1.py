t = int(input("digite um número que será o tamanho do quadrado: "))

while linha < t:
	while coluna < t:
		print("@" , end="")
		coluna += 1
	linha += 1

"""Com FOR
for i in range(0, t):
	print("@"*t") #Truque do Python para replicar um símbolo é multiplicar

Para continuar na linha através do FOR
x = int(input("Digite o lado de um retângulo: "))
y = int(input("Digite o lado de um retângulo"))
for linhas in range(0, x):
	for colunas in range (0, y):
		print("@", end="") #Truque para imprimir horizontal até o fim e depois vertical
	print()"""