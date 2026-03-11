from numpy import *
#Lista de Produtos comprados:
lista_de_produtos = array(eval(input("digite o vetor: ")))
i = 0
res = 0
while i < len(lista_de_produtos):
	if lista_de_produtos[i]>80:
		res = res + (lista_de_produtos[i] - 5)
	else:
		res = res + lista_de_produtos[i] 
	i = i + 1
print(round(res,2))
	







