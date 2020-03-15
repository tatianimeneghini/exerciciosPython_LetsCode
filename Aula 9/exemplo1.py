"""Orientação a objetos é fazer o programa se explicar.

Classes é um modelo/forma.

Objeto é um elemento criado a partir da classe. 
Todo elemento se caracteriza por atributos, informações.

Para análise de sistema, é necessário, antes de programar um sistema, modelar o problema, o planejamento do objeto, de como será resolvido.

Sintaxe:
class <nome_da_classe>():
    <atributos>"""

class Cliente(): #Criar uma classe vazia

#função construtora
    def __init__(self, nome_completo, cpf, tem_foto, endereco, telefone, email, genero, estado_civil, idade):
    	self.nome = nome_completo #Para amarrar os parâmetros aos atributos do objeto.    
    
    nome = "" #identificar o tipo de objeto. Tipo texto <"">.
    cpf = 0 #tipo número
    tem_foto = True or False #tipo lógico <True or False>
    endereco = ""
    telefone = 0
    email = ""
    genero = ""
    estado_civil = ""
    idade = 0

#Para criar objetos de uma classe, é necessário instanciar um objeto:
joao = Cliente() #Instanciação de um objeto. Sintaxe: variavel = <classe>()
joao.nome_completo = "João Santos"
joao.cpf = 123456789
joao.tem_foto = True
joao.endereco = "Rua Sol, 30 - Bairro Fazenda"
joao.email = "email@email.com.br"
joao.estado_civil = "homem cis"
joao.idade = 30

print(joao.nome)