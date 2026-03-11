#---------------------------------------------------------
# UNIVERSIDADE FEDERAL DO AMAZONAS
# ANA REBECA CAVALCANTE EVANGELISTA
# MATRICULA: 21456290
# DATA: 30/06/2016
# OBJETIVO: Media aritmetica de 4 notas dadas.
#-----------------------------------------------------------

from math import * 

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

soma = (nota1 + nota2 + nota3 + nota4)
media = soma / 4

if (media >= 6.0):
	print (round(media, 1))
	print ("Aprovado")
else:
	print (round(media, 1))
	print ("Reprovado")