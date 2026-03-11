# faça seu código aqui!

peso = float(input(""))

custo_fixo = 10

if peso < 5:
	taxa = 3.75
elif peso == 5:
	taxa = 4.75
elif peso > 5:
	taxa = 5.75

total = custo_fixo + taxa
print(total)