def soma(n1, n2):
	return n1 + n2

def sub(n1, n2):
	return n1 - n2

def mult(n1, n2):
	return n1 * n2

def divisao(n1, n2):
	return n1 / n2

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

resultado_soma = soma(n1, n2)
resultado_sub = sub(n1, n2)
resultado_mult = mult(n1, n2)
resultado_divisao = divisao(n1, n2)

print("O valor da soma é ", resultado_soma)
print("O valor da subtracao é ", resultado_sub)
print("O valor da multiplicao é ", resultado_mult)
print("O valor da divisao é ", resultado_divisao)