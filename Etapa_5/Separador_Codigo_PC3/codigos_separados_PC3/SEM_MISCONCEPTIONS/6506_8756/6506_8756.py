prato = int(input(""))
sobremesa = input("")
if sobremesa == "s":
	tudo = prato * 40 
	desconto = tudo * 5/100
	total = tudo - desconto
	print(total)
else:
	Odesconto = prato * 40
	print(Odesconto)