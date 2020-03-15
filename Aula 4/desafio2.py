contador = 0
soma = 0
fatorial = 1

while contador < 1000:
	contador += 1
	fatorial = fatorial*contador
	soma += 1/fatorial

print('O fatorial desse número é ', soma)