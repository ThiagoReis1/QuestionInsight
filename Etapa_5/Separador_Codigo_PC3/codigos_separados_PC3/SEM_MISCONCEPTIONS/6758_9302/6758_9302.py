dias = int(input("carros: "))

if dias < 7:
	valor = 100.00 * dias + 15.00
	
elif dias == 7:
	valor = 100.00 * dias  + 12.00
	
else: 
	valor = 100.00 * dias + 10.00
	
print(round(valor,2))