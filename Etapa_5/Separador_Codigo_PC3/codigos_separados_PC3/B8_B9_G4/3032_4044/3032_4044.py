'''
-------------------------------------------
 |-----------|
 | Questão 2 |
 |-----------|

 TP3 - Estrutura Condicional Encadeada
 
 Universidade Federal do Amazonas
 Instituto de Ciências Exatas
 Departamento de Física
 
 Aluno: Micael Davi Lima de Oliveira - 21851626 - FB01
 Data: 29/04/2019
-------------------------------------------
'''

x = float(input("Digite um valor(real) para x: "))

if (x <= 0):
	print("0")
elif ((x > 0) and (x <= 1)):
	print("1")
elif ((x > 1) and (x <= 2)):
	print(round(x**(1/2), 4))
elif (x > 2):
	print(round(x**(1/3), 4))