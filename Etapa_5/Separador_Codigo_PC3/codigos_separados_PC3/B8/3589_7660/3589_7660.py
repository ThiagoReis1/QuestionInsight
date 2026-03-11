#--------------------------------------------------------------
# Nome: Ivan Lucas de Oliveira Pacheco
# Data: 30/01/2023
# Objetivo: Definir a pontuação de um competidor de arco e flecha
#--------------------------------------------------------------
from numpy import*

disparos = array(eval(input("Descreva os aneis atingidos pelo competidor: ")))

cont = 0
pontos = 0
while cont < size(disparos):
	if disparos[cont] == 1:
		pontos = pontos + 80
	elif disparos[cont] == 2:
		pontos = pontos + 40
	elif disparos[cont] == 3:
		pontos = pontos + 20
	elif disparos[cont] == 4:
		pontos = pontos +10
	cont = cont + 1

print (pontos)