# faça seu código aqui!

dia = int(input(''))

taxa_fixa = 175

if dia < 15:
	taxa = 20
elif dia == 15:
	taxa = 16
else:
	taxa = 10
	
total = (taxa_fixa * dia) + taxa

print(round(total,2))

