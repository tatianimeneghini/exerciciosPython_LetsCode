n = int(input("Digite um número. "))
while n <0:
    print("Somente números inteiros positivos")
    n = int(input("Digite um número. "))

intervalo = list(range(1, n+1))
for item in intervalo:
    print("15 x item " , item , "=" , 15*intervalo)

"""numero = 1
while numero <= n:
    print("15 x " , numero , " = " , 15*numero)
    numero += 1"""