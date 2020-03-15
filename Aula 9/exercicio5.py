class Conta():
	def __init__(self, numero_conta, saldo):
		self.numero_conta = numero_conta
		self.saldo = saldo

def depositar(saldo_cliente, valor_deposito):
	r = saldo_cliente+valor_deposito
	print("Saldo depois do depósito: ", r)

def sacar(saldo_cliente, saque_conta):
	if saque_conta <= saldo_cliente:
		print("O seu novo saldo é de ", saldo_cliente-=saque_conta)		
	else:
		print("Operação inválida, valor a ser sacado é maior que seu saldo.")
#saldo = float(input("Digite sua conta: "))
#numero_conta int(input("Digite seu saldo "))

conta_carla = Conta(12345, 5000)
print("Saldo antes do depósito ", carla.saldo)

carla.saldo = sacar(conta_carla.saldo, 20)