#############################################################
# UFAM - UNIVERSIDADE FEDERAL DO AMAZONAS
# RODRIGO FONTANELLA CESTARI
# 30/06/2016
# OBJETIVO: Escreva um programa que tome as quatro notas dele 
# e mostre, alem do valor da media aritmetica, a mensagem
# “Aprovado”,caso a média seja igual ou superior a 7, ou a 
# mensagem “Reprovado”, caso contrario.
##############################################################

#notas provas
p1 = float(input("Qual a primeira nota? "))
p2 = float(input("Qual a segunda nota? "))
p3 = float(input("Qual a terceira nota? "))
p4 = float(input("Qual a quarta nota? "))
#media das 4 notas
media = (p1 + p2 + p3 + p4)/4
# nota minima para ser aprovado
minimo = 7 
#condicao
if (media >= minimo):
	print (round (media, 2))
	print ("Aprovado")
else:
	print (round (media, 2))
	print ("Reprovado")
