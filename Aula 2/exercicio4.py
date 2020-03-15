letra = str(input("Insira uma letra: "))

vogal = ["a", "e", "i", "o", "u"]
consoante = ["b", "c", "d", "f" , "g" , "h" , "j" , "k" , "l" , "m" , "n" , "p" , "q" , "r" , "s" , "t" , "v" , "w" , "y" , "x" , "z"]

if letra == vogal:
	print("A letra digitada " , letra , " é uma vogal")
if letra == consoante:
	print("A letra digitada " , letra , " é uma consoante")