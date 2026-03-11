#----------------------------------
#	UNIVERSIDADE FEDERAL DO AMAZONAS
#	LARISSA SANTOS BRITO
#	MATRICULA: 21454598
#	DATA: 30/06/2016
#	AVALIAÇÃO 02
#----------------------------------

from math import *
X = int(input(" Digite um numero:"))

valor1 = X // 10000
valor2 = X % 10000

soma = (valor1 + valor2)

if (soma ** 2 == X):
	print(X, "atende a propriedade")
else:
	resultado = (soma ** 2)
	print(resultado)


