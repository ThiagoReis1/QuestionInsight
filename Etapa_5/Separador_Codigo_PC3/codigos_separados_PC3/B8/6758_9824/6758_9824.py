# faça seu código aqui!
dias = int(input('digite os dias: '))

if dias < 7:
	aluguel = dias * 100 + 15.00
elif dias == 7:
	aluguel = dias * 100 + 12.00
elif dias > 7:
	aluguel = dias * 100 + 10.00

print(round(aluguel, 2))

	