nome = str(input("T para TAPIOCA ou S para SALGADO: "))
quant = int(input("Quantidade: "))
quanta = int(input("Quantidade acai: "))

if(nome.upper()=='T'):
	total = (quant * 3.50) + (quanta * 13.00)

if(nome.upper()=='S'):
	total = (quant * 5.00) + (quanta * 13.00)

print(round(total, 2))