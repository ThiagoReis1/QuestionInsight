dias = int(input("Quantidades de dias para alugar? "))

if dias < 7: 
	taxa = 15
	
elif dias == 7:
	taxa = 12
	
else:
	taxa = 10
	
total = 100 * dias + taxa
print(round(total,2))