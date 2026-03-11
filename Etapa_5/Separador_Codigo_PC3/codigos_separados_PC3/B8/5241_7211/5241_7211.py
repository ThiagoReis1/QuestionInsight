cons=int(input("consumo de agua: "))
taxaFixa = 20

if(cons <= 10):
	pg=cons + taxaFixa + 5.00
	print(pg)
elif(cons >= 10 or 2.5 <= 20):
	pg=cons + taxaFixa + 22.5
	print(pg)
elif(cons >= 20 or 2.75 <= 40):
	pg=cons * taxaFixa
	print(pg)
else:
	if(cons >= 40):
		pg=cons * taxaFixa



	