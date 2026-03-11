# faça seu código aqui!
entrada= input("Digite qual entrada aA, bB, cC ou dD: "). upper()
quantidade= int(input("Digite a quantidade desejada: "))
valor_entrada= 25.90
desconto= 0.10
valor_total= valor_entrada * quantidade
if (entrada.upper() == "B"):
	valor_total= valor_total - (valor_total * 0.10)
	print(round(valor_total,2))
else:
	print(round(valor_total,2))