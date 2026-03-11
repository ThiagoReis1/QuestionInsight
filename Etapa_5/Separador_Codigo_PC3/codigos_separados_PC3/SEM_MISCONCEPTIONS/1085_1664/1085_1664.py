#----------------------------------------------------------
#	UNIVERSIDADE FEDERAL DO AMAZONAS	
#	LARISSA SANTOS BRITO
#	MATRICULA: 21454598
#	DATA: 30/06/2016
#	AVALIAÇÃO 02 
# OBJETIVO : Escrever a média e verificar aprovação de aluno
#-------------------------------------------------------------
from math import *

nota_1 = float(input("digite o valor da primeira nota:"))
nota_2 = float(input("digite o valor da segunda nota:"))
nota_3 = float(input("digite o valor da terceira nota:"))
nota_4 = float(input("digite o valor da quarta nota"))
nota_5 = float(input("digite o valor da quinta nota:"))

soma = (nota_1 + nota_2 + nota_3 + nota_4 + nota_5)
media = (soma / 5)
 
if(media >= 6.0):
	print(round(media, 2))
	print("Aprovado")
else:
	print(round(media, 2))
	print ("Reprovado")
	