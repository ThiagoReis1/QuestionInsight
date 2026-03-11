tapioca_salgado= input("Insira T se for uma tapioca ou S se for um salgado: ") .upper()
quant_S_T= int(input("Insira a quantidade de salgados ou tapiocas: "))
quant_acai= int(input("Insira a quantidade de acais: "))

if tapioca_salgado == "T":
	print(round(3.5 * quant_S_T + 13 * quant_acai, 2))
	
else:
	print(round(5 * quant_S_T + 13 * quant_acai, 2))
	