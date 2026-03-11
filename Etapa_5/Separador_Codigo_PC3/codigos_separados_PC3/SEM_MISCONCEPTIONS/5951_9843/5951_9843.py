item = input("Digite T se for tapioca e S se for salgado: ")
quant = int(input("Digite a quantidade: "))
acai = int(input("Digite a quantidade comprada de acai: "))

if (item == "T"):
	conta = (quant * 4.5) + (acai * 12)
	print(conta)
	
if (item == "S"):
	conta = (quant * 5) + (acai * 12)
	print(conta)