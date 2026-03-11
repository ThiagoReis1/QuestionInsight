e = float(input("consumo: "))
conta1 = (e*0.60)+5
conta2 = (e*0.75) + 16
if (e <= 150):
	print(round(conta1, 2))
else:
	print(round(conta2, 2))