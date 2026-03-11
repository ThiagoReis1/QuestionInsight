#------------------------------------------------------------------------------
# Nome: Ivan Lucas de Oliveira Pacheco
# Data: 21/12/2022
# Objetivo: Imprimir uma mensagem baseada no numero digitado pelo usuário
#------------------------------------------------------------------------------

# Importação de bibliotecas
from math import*

# Ler o valor que corresponderá a string
numero = int(input("Digite um valor: "))

if numero >= 1:
	if ((numero % 3) == 0) and ((numero % 5) == 0):
		mensagem = "AuauMiau"
	elif ((numero % 5) == 0):
		mensagem = "Miau"
	elif ((numero % 3) == 0):
		mensagem = "Auau"
	else:
		mensagem = numero

print (mensagem)