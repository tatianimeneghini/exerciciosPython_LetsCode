from exercicio2_aula12 import Agenda, Contato

#Criando a agenda.
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

agenda.listar()
