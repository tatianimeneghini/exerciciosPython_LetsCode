produto=float(input("Estamos sofrendo um reajuste dos produtos. Digite o valor do produto que você costuma comprar e identificaremos o reajuste do valor do produto. "))
produtoFINAL = 0.

while produto < 0:
    print("Só inserir número positivos. ")
    produto=float(input("Estamos sofrendo um reajuste dos produtos. Digite o valor do produto que você costuma comprar e identificaremos o reajuste do valor do produto. "))
produtoFINAL = 0.

if produto < 50:
   produtoFINAL = produto + (produto*0.05)
if produto >= 50 and produto <= 100:
   produtoFINAL = produto + (produto*0.10)
if produto > 100 and produto <= 150:
   produtoFINAL = produto + (produto*0.13)
if produto > 150:
  produtoFINAL = produto + (produto*0.15)

print("O valor final é " , produtoFINAL)

if produtoFINAL < 80:
   print("BARATO *-*")
# Barato
if produtoFINAL >= 80 and produtoFINAL < 115:
   print("RAZOÁVEL :D")
# Razoável
if produtoFINAL < 150 and produtoFINAL >= 150:
   print("NORMAL :| ")
# Normal
if produtoFINAL >= 150 and produtoFINAL < 170:
   print("CARO :( ")
# Caro
if produtoFINAL >= 170:
   print("MUITO CARO ¬¬")
# Muito caro
