oq = input("Especifique (B)Bolo ou (S)Salgado:")
quant = int(input("Quantidade de Bolos ou salgados:"))
capu = int(input("Quantidade de cappuccinos:"))

bolo = 5.00
salgado = 4.00
cappuccino = 7.50

if oq.upper() == "B":
	a = (quant * bolo) + (capu*cappuccino)
	print(round(a,2))
else:
	a = (quant * salgado) + (capu * cappuccino)
	print(round(a,2))