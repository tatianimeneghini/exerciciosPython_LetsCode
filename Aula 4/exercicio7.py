#idade
idade = int(input("Digite sua idade: "))

while idade > 0:
	idade = int(input("Digite sua idade: "))
print("Você tem " , idade , "anos")

#salário
salario = int(input("Digite seu salário bruto: "))

while salario >= 0:
	salario = int(input("Digite sua idade: "))
print("Você recebe " , salario)

#sexo
sexo = int(input("Qual seu sexo? Insira 1 para feminino, 2 para masculino e 3 para não binário: "))

while sexo != 1 and sexo != 2 and sexo != 3:
	sexo = int(input("Qual seu sexo? Insira 1 para feminino, 2 para masculino e 3 para não binário: "))

print("Acabou!")