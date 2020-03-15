n1 = int(input("Digite um número "))
n2 = int(input("Digite um número "))
n3 = int(input("Digite um número "))
n4 = int(input("Digite um número "))

if n1 > n2:
	print("O primeiro número é MAIOR que o segundo")
if n1 > n3:
	print("O primeiro número é MAIOR que o terceiro")
if n1 > n4:
	print("O primeiro número é MAIOR que o quarto")
if n2 > n3:
	print("O segundo número é MAIOR que o terceiro")
if n2 > n4:
	print("O segundo número é MAIOR que o quarto")
if n4 > n1:
	print("O quarto número é MAIOR que o primeiro")
if n4 > n2:
	print("O quarto número é MAIOR que o segundo")
if n4 > n3:
	print("O quarto número é MAIOR que o terceiro")

if n1 < n2:
	print("O primeiro número é MENOR que o segundo")
if n1 < n3:
	print("O primeiro número é MENOR que o terceiro")
if n1 < n4:
	print("O primeiro número é MENOR que o quarto")
if n2 < n3:
	print("O segundo número é MENOR que o terceiro")
if n4 < n3:
	print("O terceiro número é MENOR que o quarto")

if n1 == n2:
	print("O primeiro número é IGUAL que o segundo")
if n3 == n2:
	print("O segundo número é IGUAL que o terceiro")
if n1 == n3:
	print("O primeiro número é IGUAL que o terceiro")
if n4 == n1:
	print("O quarto número é IGUAL que o primeiro")
if n4 == n2:
	print("O quarto número é IGUAL que o segundo")
if n4 == n3:
	print("O quarto número é IGUAL que o terceiro")