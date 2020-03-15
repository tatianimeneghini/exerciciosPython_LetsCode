""""Estruturas de dados - organizam dados.
1. Lista: sequência de elementos, pode ser modificada.
2. Tupla:sequência de elementos, nao pode ser modificada. Mantém os dados consistentes.
3. Dicionário: uma chave que leva a um valor, pode ser modificada."""

def soma(a, b):
	soma = a + b
	sub = a - b
	return soma, sub #Quando há mais de um valor no return, uma tupla é retornada.


A = [2, 3, 4] #Lista
B = (2, 3, 4) #Tupla

A[0] #Para acessar algum índice sequencial da lista. Posicao 0 é o primeiro elemento sempre.
B[1]

"""Agregar algum elemento na lista é só utilizar .append(). A tupla nao pode ser modificada"""
A.append(9) #Para remover algum elemento da lista .remove().

B = list(B) #Para modificar a tupla, seria necessário uma gambiarra, que transforma ela em lista, faz a modificacao e depois returna a lista em tupla.
B.append(9)
B = tuple(B)