from exercicio1_aula12 import ControleRemoto

controle1 = ControleRemoto(10,18)

controle1.ConsultarCanal()

controle1.AumentarVolume()
print("O volume da televisão está em ", controle1.volume)

controle1.AumentarCanal()
controle1.ConsultarCanal()

controle1.DefinirCanal(5)
controle1.ConsultarCanal
