#O input tem a ver com os parâmetros. O print é um parâmetro. Espera-se, conforme acordo da programacao, só coloca a acao da funcao. 
#No caso do print, como nao se refere exatamente à funcao, é só colocar fora.
#O output vai ser a saída do programa, o retorno (return) na última linha da funcao

def soma(a, b, c):
	s = a + b + c
	return s

cesta = imprime("lets code")

#Se tem return, tem que haver uma outra variável da chamada da funcao

def media (a, b, c):
#	s = soma(a, b, c)
#	media = s/3 #Pra cortar os intermediários.
	media = soma(a, b, c)/3
	return media	

numero1 =int(input("digite um numero: "))
numero2=int(input("digite outro numero: "))
numero3=int(input("digite outro número: "))

print(cesta)
print(s)