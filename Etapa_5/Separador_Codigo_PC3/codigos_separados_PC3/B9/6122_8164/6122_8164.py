comb = float(input("quantidade de combustivel: "))
if comb < 17.5:
	quant = comb + 0.8
	print(round(quant,2))
elif comb >= 17.5 and comb < 35.0:
	quant = comb + 1.3
	print(round(quant,2))
elif comb >= 35.0 and comb < 50.0:
	quant = comb + 2.1
	print(round(quant,2))
else:
	quant = comb + 3.0
	print(round(quant,2))