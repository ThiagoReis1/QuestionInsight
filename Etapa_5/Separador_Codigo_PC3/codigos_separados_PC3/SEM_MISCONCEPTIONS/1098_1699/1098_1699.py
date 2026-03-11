#----------------------------------------------------------
# UNIVERSIDADE FEDERAL DO AMAZONAS
# ANA REBECA CAVALCANTE EVANGELISTA
# MATRICULA: 21456290
# DATA: 30/06/2016
# OBJETIVO: Encontrar um número que satisfaça a condição dada.
#------------------------------------------------------------

from math import *

X = int(input("Digite um numero de 6 digitos: "))

valor_1 = X // 1000  
valor_2 = X % 1000
diferenca = ( valor_1 - valor_2 )

if(diferenca ** 4 == X):
	print (X, "atende a propriedade")
else:
	resultado = (diferenca ** 4) 
	print (resultado)  