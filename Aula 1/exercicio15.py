metros = float(input("Digite o tamanho em metros quadrados da área a ser pintada: "))

litros = metros / 3
print("A quantidade de litros necessária é ", litros)

latas = litros/18
print("A quantidade de lata para comprar é ", latas)

preco_total = latas * 80
print("O valor total é: R$ " , preco_total)