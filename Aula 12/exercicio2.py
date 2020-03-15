class Agenda():
    def __init__(self):
        self.contatos = []
        
    def add(self, novo_contato):
        self.contatos.append(novo_contato)
        
    def remove(self, nome_busca):
        for contato in self.contatos:
            if contato.nome == nome_busca:
                self.contatos.remove(contato)
                return
        print("O contato não foi encontrado! :( ")

    def buscar(self, nome_busca):
        for contato in self.contatos:
            if contato == nome_busca:
                return contato
        print("O contato não foi encontrado! :( ")
        
    def listar(self):
        for contato in self.contatos:
            print(contato.nome, contato.telefone)
            
class Contato():
    def __init__(self, nome, telefone, email, endereco):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco
        self.is_blocked = False #É um atributo, mas não faz parte do parâmetro.

    def edit(self):
        novo_nome = input("Digite o novo nome do contato: ")
        novo_telefone = input("Digite o novo telefone do contato: ")
        novo_email = input("Digite o novo e-mail do contato: ")
        novo_endereco = input("Digite o novo endereço do contato: ")

        self.nome = novo_nome
        self.telefone = novo_telefone
        self.email = novo_email
        self.endereco = novo_endereco

    def block(self):
        self.is_blocked = True

    def unlock(self):
        self.is_blocked = False  
