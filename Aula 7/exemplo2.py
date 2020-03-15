"""O dicionario é uma estrutura que possui uma chave e leva a um conjunto de valores.
key -> valores

dicionario = {key:valor} ou dicionario = dict({key:valor})"""

dicio = {}
dicio = {"dog": "cachorro", "cat":"gato", "tree":"arvore"} #Para percorrer os valores de um dicionário, está em valor, nao na key/chave.

print(dicio["dog"])

dicio.update({"river":"rio"}) #Para adicionar elementos: .update() ao dicionário.

for i in dicio
	print(i)

print(dicio.keys()) #O comando .keys() lista as chaves do dicionário.
print(dicio.values()) #O comando .values() lista os valores do dicionário.

del dicio["river"] #O comando del apaga o par da chave.