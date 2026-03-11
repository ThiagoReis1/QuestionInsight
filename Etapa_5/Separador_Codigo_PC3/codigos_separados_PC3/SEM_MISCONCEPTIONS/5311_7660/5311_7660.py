#-------------------------------------------------
# Nome: Ivan Lucas de Oliveira Pacheco
# Data: 11/01/2023
# Objetivo: Definir o valor final de uma aplicação financeira
#-------------------------------------------------

taxa = 0.012
n = 0

montante = float(input("Qual o valor da aplicacao? "))
periodo = int(input("Defina a quantidade de meses da aplicaca: "))

while n < periodo:
	montante = montante * (1 + taxa)
	n = n + 1
	print (round(montante,2))
