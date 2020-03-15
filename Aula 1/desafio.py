velocidade_inicial = float(input("Digite a velocidade inicial em metros: "))
posicao_inicial = float(input("Digite a posiciao inicial em metros: "))
tempo = float(input("Digite o tempo de deslocamento em minutos: "))

posicao_final = posicao_inicial + (velocidade_inicial * tempo) + (9.8 * tempo**2)/2

print("A velocidade final é " , posicao_final)