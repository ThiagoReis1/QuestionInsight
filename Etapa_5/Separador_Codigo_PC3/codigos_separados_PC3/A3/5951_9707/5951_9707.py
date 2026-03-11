nome = str(input("T para Tapioca ou S"))
quant = int(input("Quantidade: "))
quanta = int(input("Quantidade acai: "))


if(nome.upper()=="T"):
	total = (quant * 4.50) + (quanta * 12.00)
	
if(nome.upper()=="S"):
	total = (quant * 5.00) + (quanta * 12.00 )
	
print(total)