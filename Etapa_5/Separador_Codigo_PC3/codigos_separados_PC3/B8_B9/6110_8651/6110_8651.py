quant = int(input("quantidade de comb comum: "))

if quant<17.5:
	total = quant + 10.5
elif quant>=17.5 and quant<35:
	total= quant + 14
elif quant>=35 and quant<50:
	total = quant + 18.6
elif quant>=50:
	total = quant + 24.5
print(round(total,1))