dias = int(input(""))
valor_total = 0
if dias < 7:
	valor_total = dias*100 + 15.00
	
elif dias == 7:
	valor_total = dias*100 + 12.00
		
else:
	valor_total = dias*100 + 10.00
	
print(round(valor_total, 2))