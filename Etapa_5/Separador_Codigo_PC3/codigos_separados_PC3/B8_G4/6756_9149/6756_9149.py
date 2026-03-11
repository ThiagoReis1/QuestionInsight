# faça seu código aqui!
dias = int(input("quantidades de dias reservado: "))

if dias < 15:
	taxa = dias * 175.0 + 20.0
elif dias == 15:
	taxa = dias * 175.0 + 16.0
elif dias > 15:
	taxa = dias * 175.0 + 10.0
	
print(round(taxa, 2))

