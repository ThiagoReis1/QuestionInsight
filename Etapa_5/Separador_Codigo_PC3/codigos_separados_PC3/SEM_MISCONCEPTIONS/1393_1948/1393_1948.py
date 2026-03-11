#--------------------------------------------------
#Universidade Federal do Amazonas
#Larisse Gabriele Ramos de Abreu
#Data: 22/11/2016
#
#Objetivo: Cobranca de frete
#---------------------------------------------------

from math import*

peso_da_encomenda = int(input("Peso da encomenda: "))
if(peso_da_encomenda < 5000):
	print(round(peso_da_encomenda * 0.05, 2))
else:
	x = (peso_da_encomenda * 0.04) + 60.00
	print(round(x, 2))