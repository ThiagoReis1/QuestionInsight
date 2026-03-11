bc = input("B para Bolo ou C para Croissant: ")
qfc = int(input("Quantidade de fatias de Bolo ou Croissant: "))
qc = int(input("Quantidade de Cappuccinos: "))

if (bc.upper() == "B"):

	total = qfc*3+qc*5.5
	
else:
	
	total = qfc*6+qc*5.5
	
print(round(total,2))