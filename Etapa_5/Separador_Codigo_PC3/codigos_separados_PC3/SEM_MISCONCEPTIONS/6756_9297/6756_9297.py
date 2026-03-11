dias = int(input("dias reservados: "))

if dias < 15:
	taxa = 20.00
elif dias == 15:
	taxa = 16.00
else:
	taxa = 10.00
	
hospedagem = 175.00 * dias + taxa 
print(round(hospedagem, 2))