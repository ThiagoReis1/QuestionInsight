opcao = input("T para tapioca e S para salgado: ").upper()
quant = int(input("Quantidade: "))
quant_acai = int(input("Quantidade de acais: "))

total = 0

if opcao == "T":
	total = quant * 4.5 + quant_acai * 12
	print(round(total,2))
else:
	total = quant * 5 + quant_acai * 12
	print(round(total,2))