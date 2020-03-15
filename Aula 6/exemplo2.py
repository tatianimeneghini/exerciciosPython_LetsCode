"""def media ():
	x = int(input("Digite um número "))
	y = int(input("Digite outro número "))
	z = int(input("Digite outr número "))

	nota_final = (x+y+z) / 3

print("A média é ", nota_final)"""

#Funcoes: entrada (declarando, criando a variável) e saída (retorno pro programa)
#Se a variável está fora da funcao, se torna uma variavel global. Variaveis que estao dentro da funcao, é considerada uma variável local.

#O parâmetro/argumento da funcao (x em f(x)) substitui na mesma linha do def dentro dos parânteses:

def media (a, b, c):
	#nota_final = (x+y+z) / 3 #variavel local
	nota_final = (a + b +c) / 3
	print("A média é ", nota_final)

x = int(input("Digite um número ")) #variáveis globais
y = int(input("Digite outro número "))
z = int(input("Digite outr número "))
media(x, y, z)
