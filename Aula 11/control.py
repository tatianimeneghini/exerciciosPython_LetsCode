from model import Cachorro, Gato

bilu = Cachorro("Bilu", "Yorkshire", "pequeno", "João")
print(bilu.nome)
bilu.latir()
bilu.correr()
bilu.morder()

#Equivalente ao Control. Os arquivos têm de estar na mesma pasta, mesmo diretório.
xuxu = Gato("Xuxu", "sem raça", "Tats")
print("Xuxu é a gata de "+xuxu.dono)
xuxu.pular()
xuxu.miar()
xuxu.ronronar()