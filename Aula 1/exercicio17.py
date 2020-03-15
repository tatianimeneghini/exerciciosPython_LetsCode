tamanho_arquivo = float(input("Insira o tamanho do arquivo para download em MB "))
velocidade_internet = float(input("Insira o tamanho de velocidade da internet em Mbps "))

tempo_download = tamanho_arquivo / velocidade_internet

print("O tempo aproximado de download será, em minutos " , tempo_download)