prec = float(input("valor: "))
cod = int(input("codigo da regiao: "))

desc = 40/100

if (cod == 1):
	fret= 10
	total = (prec - prec * desc) + (prec * fret/100)
	print(round(total,2))
elif cod == 2 :
	fret2 = 8
	total2 = (prec - prec * desc) + (prec * fret2 /100)
	print(round(total2,2))
elif cod == 3:
	fret3 = 0
	total3 = (prec - prec * desc) + (prec * fret3 / 100)
	print(round(total3,2))
elif cod ==4 :
	fret4 = 2
	total4 = (prec - prec * desc) + (prec * fret4 / 100)
	print(round(total4,2))