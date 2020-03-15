n1 = int(input("Digite um número "))
n2 = int(input("Digite um número "))
n3 = int(input("Digite um número "))

if n1 > n2:
	print("O primeiro número é MAIOR que o segundo")
if n2 > n3:
	print("O segun do número é MAIOR que o terceiro")
if n1 > n3:
	print("O primeiro número é MAIOR que o terceiro")

if n1 < n2:
	print("O primeiro número é MENOR que o segundo")
if n1 < n3:
	print("O primeiro número é MAIOR que o terceiro")
if n1 < n3:
	print("O primeiro número é MAIOR que o terceiro")

if n1 == n2:
	print("O primeiro número é IGUAL que o segundo")
if n3 == n2:
	print("O segundo número é IGUAL que o terceiro")
if n1 == n3:
	print("O primeiro número é IGUAL que o terceiro")
