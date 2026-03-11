# faça seu código aqui!
dias_aluguel = int(input())
diaria = dias_aluguel * 100.00

if dias_aluguel < 7:
	var = diaria + 15.00
elif dias_aluguel == 7:
	var = diaria + 12.00
else:
	var = diaria + 10.00
print(round(var, 2))