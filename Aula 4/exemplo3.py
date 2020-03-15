numero_usuario=int(input("digite um número: "))

soma = 0 
intervalo=0

while intervalo <= numero_usuario:
	print(intervalo)
	soma += intervalo
	intervalo += 1
print("While: a soma total é " , soma)