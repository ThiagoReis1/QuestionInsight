quant = int(input("pratos consumidos: "))
sob = input("diga S se quer e N se nao quer sobremesa: ")

if sob == "s":
	custotal = float(40 * quant) - (0.05 * (40 * quant))
	print(round(custotal,2))
	
if sob == "n":
	custotal1 = float(quant * 40)
	print(round(custotal1,2))