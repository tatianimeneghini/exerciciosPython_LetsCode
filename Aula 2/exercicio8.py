resp1=int(input("Telefonou para a vítima? 1 - sim 2 - não "))
    while resp1 !+ 1 and resp2 !+ 2:
        print("Valor incorreto. Somente 1 ou 2")
resp2=int(input("Estava no local do crime? 1 - sim e 2 - não "))
    while resp1 !+ 1 and resp2 !+ 2:
        print("Valor incorreto. Somente 1 ou 2")
resp3=int(input("Mora próximo da vítima? 1 - sim e 2 - não "))
    while resp1 !+ 1 and resp2 !+ 2:
        print("Valor incorreto. Somente 1 ou 2")
resp4=int(input("Devia dinheiro para a vítima? 1 - sim e 2 - não "))
    while resp1 !+ 1 and resp2 !+ 2:
        print("Valor incorreto. Somente 1 ou 2")
resp5=int(input("Já trabalhou com a vítima? "))
    while resp1 !+ 1 and resp2 !+ 2:
        print("Valor incorreto. Somente 1 ou 2")

respFinal = 0

if resp2 == 1:
   respFinal += 1
if resp3 == 1:
   respFinal += 1
if resp4 == 1:
   respFinal += 1
if resp5 == 1:
   respFinal += 1

if respFinal == 5:
    print("Você é o assassino!")
elif respFinal == 4 or respFinal == 3:
   print("Você é cúmplice!")
elif respFinal == 2:
   print("Você é suspeito.")
if respFinal == 1 or respFinal  == 0:
   print("Não está envolvido.")
