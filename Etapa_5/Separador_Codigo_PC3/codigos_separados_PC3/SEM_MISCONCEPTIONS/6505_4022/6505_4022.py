tipo = input("tipo de combo: ").upper()
quant = int(input("quant de combo: "))

a = 30.

total = a * quant

if(tipo == "c" ):
	desc = total * 15/100
	print(round(desc, 2))

else:
	print(round(total, 2))
