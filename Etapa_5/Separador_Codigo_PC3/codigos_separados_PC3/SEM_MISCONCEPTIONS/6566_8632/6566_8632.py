# faça seu código aqui!
quant = int(input("quant: "))

if quant < 10:
	total = 30 + 3.25
elif quant == 10:
	total = 30 + 4.50
else:
	total = 30.00 + 6.00
print("total=", round(total, 2))