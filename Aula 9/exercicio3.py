class Cliente():
    def __init__(self, nome1, cpf1, tem_foto1, endereco1, telefone1, email1, genero1, estado_civil1, idade1):
        self.nome = nome1 #Lado esquerdo são atributos. O self serve como obrigar o Python a reconhecer o primeiro atributo.
        self.cpf = cpf1 #Lado direito são parâmetros.
        self.tem_foto = tem_foto1
        self.endereco = endereco1
        self.telefone = telefone1
        self.email = email1
        self.genero = genero1
        self.estado_civil = estado_civil1
        self.idade = idade1

joao = Cliente("João Soares", 123456789, True, "Rua Nuvem, 2 - Jardim Céu", 1186592485, "joao@email.com.br", "homem cis", "solteiro", 30)

print(joao.endereco)
print(joao.telefone)
