T_S = input("tapioca ou salgado(T/S):")
quant = int(input("quant de merenda: "))
quant2 = int(input("quant de acai: "))


if T_S == "T":
	merenda = quant * 5.50
	acai = quant2 * 10.0
	total = merenda + acai
	
else:
	merenda = quant * 4.0
	acai = quant2 * 10.0
	total = merenda + acai
print(round(total, 2))