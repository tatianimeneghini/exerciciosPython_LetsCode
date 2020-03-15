from exercicio2_aula12 import Agenda, Contato
import tkinter

tela = tkinter.Tk()

container_titulo = tkinter.Frame(tela)
cotainer_titulo.pack()

label_titulo = tkinter.Label(container_titulo)
label_titulo["text"] = "Agenda"
label_titulo.pack()

container_nome = tkinter.Frame(tela)
container_nome.pack()

label_nome = tkinter.Label(container_nome)
label_nome["text"]="Nome"
label_nome.pack(side=tkinter.LEFT) #Label estará sempre do lado esquerdo

texto_nome = tkinter.Entry(container_nome)
texto_nome.pack(side=tkinter.RIGHT)

container_telefone = tkinter.Frame(tela)
container_telefone.pack()

label_telefone = tkinter.Label(container_telefone)
label_telefone["text"]="Telefone"
label_telefone.pack()

texto_telefone = tkinter.Entry(container_telefone)
texto_telefone.pack(side=tkinter.RIGHT)

container_email = tkinter.Frame(tela)
container_email.pack()

label_email = tkinter.Label(container_email)
label_email["text"]="E-mail"
label_email.pack(side=tkinter.LEFT)

texto_email = tkinter.Entry(container_email)
texto_email.pack(side=tkinter.RIGHT)

container_endereco = tkinter.Frame(tela)
container_endereco,pack()

label_endereco = tkinter.Label(container_endereco)
label_endereco["text"]="Endereço"
label_endereco.pack(side=tkinter.LEFT)

texto_endereco = tkinter.Entry(container_endereco)
texto_endereco.pack(side=tkinter.RIGHT)

tela.mainloop()

"""#Criando a agenda.
agenda = Agenda()

#Criando o primeiro contato.
ana = Contato("Ana", "96592-6589", "ana@email.com", "Rua Sol, 58 - Céu")
paula = Contato("Paula", "96041-8450", "pmorais@gmail.com", "Rua do Amor, 1 - Onde quiser")
patricia = Contato("Patricia", "99239-8226", "patmeneghini@gmail.com", "Rua Mar, 25 - Oceano")
joao = Contato ("Joao", "99969-8562", "joao@email.com", "Rua Não sei, 85 - Foda-se")

agenda.add(paula)
agenda.add(patricia)
agenda.add(ana)
agenda.add(joao)
#Adicionar o contato na agenda.

agenda.listar()
#Listar contatos adicionados.

agenda.remove("Joao")

agenda.listar()"""
