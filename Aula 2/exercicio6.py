nota1 = float(input("Insira sua nota da primeira prova: "))
nota2= float(input("Insira sua nota da segunda prova: "))
nota3 = float(input("Insira sua nota da terceira prova: "))

media = nota1 + nota2 + nota3 / 3

if media >= 6:
   print("Você foi aprovado na disciplina. Parabéns!")
else: 
   print("Você foi reprovado na disciplina. Fale com o seu professor.")
