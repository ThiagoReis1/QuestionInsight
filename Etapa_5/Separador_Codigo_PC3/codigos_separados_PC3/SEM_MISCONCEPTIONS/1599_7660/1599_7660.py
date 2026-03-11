#--------------------------------------------------------------------
# Nome: Ivan Lucas de Oliveira Pacheco
# Data: 30/01/2023
# Objetivo: Calcular o custo de uma compra considerando desconto individual por item 
#--------------------------------------------------------------------
from numpy import*

precos = array(eval(input("Descreva os valores dos itens de compra: ")))

cont = 0
compra = 0
while cont < size(precos):
	if precos[cont] > 80:
		compra = compra + (precos[cont] * 0.85)
	else:
		compra = compra + precos[cont]
	cont = cont +1

print (round(compra,2))