def circunferencia (R):
    return 2*pi*R

pi = 3.14
R = int(input("Insira a medida do raio de um círculo: "))
C = circunferencia(R) #Lembrar de inserir sempre uma nova variável quando tiver return

print("A circunferência tem o total de ", C)