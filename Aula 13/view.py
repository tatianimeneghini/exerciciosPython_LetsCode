from exercicio2_aula12 import Agenda, Contato
import tkinter

class TelaInicial():
    def __init__(self):

def adicionar():
    nome = texto_nome.get()
    telefone = texto_telefone.get()
    email = texto_email.get()
    endereco = texto_endereco.get()

    contatinho = Contato(nome, telefone, email, endereco)
    print(contatinho.nome, contatinho.email, contatinho.endereco)
