h = int(input("horas: "))
qtde = int(input("qtde: "))

total = (qtde*28.5) - ((20/100)*28.5*qtde)
total2 = (qtde*28.5)

if (h >= 18):
	print(round(total,2))
else:
	
	print(round(total2,2))
	