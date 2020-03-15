class Televisao():
    def __init__(self, volume, canal):
        self.volume = volume
        self.canal = canal
        
class ControleRemoto(Televisao):
    def __init__(self, volume, canal):
        Televisao.__init__(self, volume, canal)

    def AumentarVolume(self):
        self.volume += 1
    
    def DiminuirVolume(self):
        self.volume -= 1
    
    def AumentarCanal(self):
        self.canal += 1
    
    def DiminuirCanal(self):
        self.canal -= 1
    
    def DefinirCanal (self, novo_canal):
        self.canal = novo_canal
    
    def ConsultarCanal(self):
        print("Você está assistindo ao canal ", self.canal)
