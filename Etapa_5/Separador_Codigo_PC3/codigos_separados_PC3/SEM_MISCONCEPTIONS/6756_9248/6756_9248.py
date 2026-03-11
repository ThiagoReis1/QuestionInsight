dias = int(input('quantidade de dias reservados: '))

if dias < 15:
	taxa = 20
	
elif dias == 15:
	taxa = 16
	
else:
	taxa = 10
	
valor = (dias * 175) + taxa
print(round(valor, 2))