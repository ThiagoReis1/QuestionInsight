comida = input("Digite T para tapioca ou S para salgado: ")
quant = int(input("Digite a quantidade de tapiocas ou salgados: "))
bebida = int(input("Digite a quantidade de acais: "))


if(comida == "T"):
	valor = (5.50 * quant) + (10.00 * bebida)
	print(round(valor,2))

if(comida == "S"):
	valor = (4.00 * quant) + (10.00 * bebida)
	print(round(valor,2))