#------------------------------------------------------------
# Nome: Ivan Lucas de Oliveira Pacheco
# Data: 30/01/2023
# Objetivo: Determinar o custo de uma etiqueta com base nos caracteres da mesma
#------------------------------------------------------------

etiqueta = input("Qual a etiqueta? ")
etiqueta = etiqueta.lower()

cont = 0
vogais = 0
outros = 0
while cont < len(etiqueta):
	if etiqueta[cont] == "a":
		vogais = vogais + 1
	elif etiqueta[cont] == "e":
		vogais = vogais + 1
	elif etiqueta[cont] == "i":
		vogais = vogais + 1
	elif etiqueta[cont] == "o":
		vogais = vogais + 1
	elif etiqueta[cont] == "u":
		vogais = vogais + 1
	cont = cont + 1

preco = (vogais * 0.12) + ((len(etiqueta) - vogais) * 0.18)

print (round(preco,2))