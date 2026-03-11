# faça seu código aqui!
idade = int(input(" "))

preco = 20.00

if idade < 12:
	taxa = 1.25
	
elif idade == 12:
	taxa = 2.25
	
elif idade > 12:
	taxa = 3.25

custo_total = preco + taxa
print(round(custo_total, 2))