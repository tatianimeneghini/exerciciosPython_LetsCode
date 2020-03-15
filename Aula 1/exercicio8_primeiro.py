hora_trabalho = float(input("Quanto você ganha por hora? "))
trabalho_mes = int(input("Quantas horas você trabalha por mês? "))

salarioBruto = hora_trabalho * trabalho_mes
print("Seu salário bruto é: R$ " , salarioBruto)

imposto_renda = salarioBruto / 1.1
print("O valor pago para o Imposto de Renda foi: R$ " , imposto_renda)

inss = salarioBruto / 0.8
print("O valor pago para o INSS foi: R$ " , inss)

sindicato = salarioBruto / 0.5
print("O valor pago para o Sindicato foi: R$ " , sindicato)

salarioLiquido = salarioBruto - imposto_renda - inss - sindicato
print("Seu salário líquido é: R$ " , salarioLiquido)