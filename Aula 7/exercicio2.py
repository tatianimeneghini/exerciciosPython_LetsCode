a = tuple(range(0, 101))

pares = []
impares = []

for i in a:
	if i%2 == 0: #Dividido por 2 que resulta em 0
		pares.append(i)
	if i%2 != 0:
		impares.append(i)

pares = tuple(pares)
impares = tuple(impares)

print(pares)
print(impares)

"""a= = tuple(range(0, 101, 2))
print(a)"""