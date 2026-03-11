quant = int(input(" Digite o valor do consumo em metros cubicos: "))



if quant < 10:
	total = 2*quant+20
	print(round(total, 2))
elif 10<=quant and quant<20:
	total = 2.5*quant+20
	print(round(total, 2))
elif 20<=quant and quant<40:
	total = 2.75*quant+20
	print(round(total, 2))
else:
	total = 3.0*quant +20
	print(round(total, 2))