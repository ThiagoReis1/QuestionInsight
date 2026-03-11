'''
---------------------------------------------------------
 |-----------|
 | Questão 1 | 
 |-----------|
 
 TP3 - Estrutura Condicional Encadeada
 
 Universidade Federal do Amazonas
 Instituto de Ciências Exatas
 Departamento de Física
 
 Aluno: Micael Davi Lima de Oliveira - 21851626 - FB01 
 Data: 29/04/2019 
----------------------------------------------------------
'''

ouro = int(input("Digite a quantidade total de pecas de ouro(PO): "))
armadura = input("Armaduras disponiveis: MALHA - PLACA - INTEIRA \n * Armadura escolhida: ")
d = int(input("Digite o fator de destreza do jogador(1-8): "))

if (d >= 1) and (d <= 8):
	if (armadura == "INTEIRA"):
		if (ouro >= 200):
			print((30*d) - 20)			
		else:
			print("PO insuficiente")
	elif (armadura == "MALHA"):
		if (ouro >= 50):
			print((15*d) - 1)
		else:
			print("PO insuficiente")
	elif (armadura == "PLACA"):
		if (ouro >= 100):
			print((20*d) - 18)		
		else:
			print("PO insuficiente")
	else:
		print("Entrada invalida")
else:
	print("Entrada invalida")
