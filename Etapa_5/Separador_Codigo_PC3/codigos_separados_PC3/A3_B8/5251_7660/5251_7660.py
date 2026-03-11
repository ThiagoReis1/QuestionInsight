#-------------------------------------------------------------
# Nome: Ivan Lucas de Oliveira Pacheco
# Data: 21/12/2022
# Objetivo: Determinar o preço a ser pago em uma passagem de barco
#-------------------------------------------------------------

# Definição do desconto
desconto = 0

# Ler cidade de destino e idade do passageiro
cidade = input("Qual a cidade de destino? ")
idade_passageiro = int(input("Informe a idade do passageiro(a): "))

cidade = cidade.lower()

# Alteração do desconto de acordo com a idade
if (idade_passageiro > 0) and (idade_passageiro < 151):
	if idade_passageiro < 3:
		desconto = 1
	elif idade_passageiro < 13:
		desconto = 0.5
	elif idade_passageiro > 64:
		desconto = 0.3
	if cidade == "porto velho":
		valor = 500
		valor = round(valor * (1 - desconto),2)
		print ("Passagem: R$", valor)
	elif cidade == "santarem":
		valor = 370
		valor = round(valor * (1 - desconto),2)
		print ("Passagem: R$", valor)
	elif cidade == "belem":
		valor = 600
		valor = round(valor * (1 - desconto),2)
		print("Passagem: R$", valor)
	elif cidade == "tefe":
		valor = 360
		valor = round(valor * (1 - desconto),2)
		print("Passagem: R$", valor)
	elif cidade == "tabatinga":
		valor = 550
		valor = round(valor * (1 - desconto),2)
		print("Passagem: R$", valor)
	else:
		valor = "Entradas invalidas"
		print (valor)
else:
	valor = "Entradas invalidas"
	print (valor)



	