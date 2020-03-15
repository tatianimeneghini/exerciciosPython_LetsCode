a = int(input("Sente dor no corpo? Digite 1 para SIM e 2 para NÃO: "))
b = int(input("Você tem febre? Digite 1 para SIM e 2 para NÃO: "))
c = int(input("Você tem tosse? Digite 1 para SIM e 2 para NÃO: "))
d = int(input("Está com congestão nasal? Digite 1 para SIM e 2 para NÃO: "))
e = int(input("Tem manchas pelo corpo? Digite 1 para SIM e 2 para NÃO: "))

if a == 1 and b == 1 and e == 1:
    print("Seus sintomas são de DENGUE. Procure um posto de saúde com urgência!")
elif a == 1 and b == 1 and c == 1 and d == 1:
    print("Seus sintomas são de GRIPE. Desancase e se alimente bem!")
elif b == 1 and c == 1 and d == 1:
    print("Seus sintomas são de GRIPE. Desancase e se alimente bem!")
elif a == 1 and c == 1 and d == 1:
    print("Seus sintomas são de GRIPE. Desancase e se alimente bem!")
elif a == 1:
    print("Você não tem nenhum sintoma. Talves seja necessário só pegar leve com seu corpo!")
elif a == 2:
    print("Você não tem nenhum sintoma. Você está saudável!")

elif a != 1 or a != 2:
    print("Só digitar 1 para SIM e 2 para NÃO. Tente responder as perguntas novamente.")
elif b != 1 or b != 2:
    print("Só digitar 1 para SIM e 2 para NÃO. Tente responder as perguntas novamente.")
elif c != 1 or c != 2:
    print("Só digitar 1 para SIM e 2 para NÃO. Tente responder as perguntas novamente.")
elif d != 1 or d != 2:
    print("Só digitar 1 para SIM e 2 para NÃO. Tente responder as perguntas novamente.")
elif e != 1 or e != 2:
    print("Só digitar 1 para SIM e 2 para NÃO. Tente responder as perguntas novamente.")