item = input("T ou S: ")
quant = int(input("Quantidade de tapioca ou salgado: "))
quant1 = int(input("Quantidade de acai: "))

if(item == "T"):
	total = (5.50 * quant) + (10 * quant1)
else:
	total = (4.00 * quant) + (10 * quant1)
	
print(total)
