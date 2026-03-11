# faça seu código aqui!
dias = int(input("insira o numero de dias: "))


if dias < 15:
	total = dias * 175 + 20
elif dias == 15:
	total = dias * 175 + 16
elif dias > 15:
	total = dias * 175 +10

	
print("total=", round(total,1))