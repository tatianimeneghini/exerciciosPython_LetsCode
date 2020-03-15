"""Existem diferenças entre dados inválidos e erros.
O erro para a execução d eum programa.
O <try/except> serve para tratar erros.

Sintaxe:
try:
    <ação a ser tratada>
except(<erro>):
    <ação de tratamento)"""

try:
    nota1 = int(input("Digite sua primeira nota: "))
except(ValueError): #Valor errado. 
    print("Valor inválido!")
#Exception: trata todos tipos de erros possíveis.

try:
    nota2 = int(input("Digite sua segunda nota: "))
except(ValueError):
    print("Valor inválido!")

try:
    nota3 = int(input("Digite sua terceira nota: "))
except (ValueError):
    print("Valor inválido!")
    
media = (nota1 + nota2 + nota3) / 3

print("A média é ", media)