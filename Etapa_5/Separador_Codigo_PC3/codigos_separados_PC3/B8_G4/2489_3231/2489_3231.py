d = input()
i = int(input())
print("Entradas:", d, ",", i)
if((d=="Porto Velho" or d=="Santarem" or d=="Belem" or d=="Tefe" or d=="Tabatinga") and i>0 and i<150):
		if (d == "Porto Velho"):
			p = 500
		elif (d == "Santarem"):
			p = 370
		elif (d == "Belem"):
			p = 600
		elif (d == "Tefe"):
			p = 360
		elif (d == "Tabatinga"):
			p = 550

		if (i==2):
			x = 0
			print("Passagem: R$", x)
		elif (i>=3 and i<=12):
			x = p / 2
			print("Passagem: R$", x)
		elif (i >= 65):
			x = p - (p * 0.3)
			print("Passagem: R$", x)
else:
	print("entradas invalidas")