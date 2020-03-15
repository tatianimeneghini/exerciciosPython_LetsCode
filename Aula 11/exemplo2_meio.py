from model import Gato

#Equivalente ao Control. Os arquivos têm de estar na mesma pasta, mesmo diretório.
xuxu = Gato("Xuxu", "sem raça", "Tats")
print("Xuxu é a gata de "+xuxu.dono)
xuxu.pular()
xuxu.miar()
xuxu.ronronar()