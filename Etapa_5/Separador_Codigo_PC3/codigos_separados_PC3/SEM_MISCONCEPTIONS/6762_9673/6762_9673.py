# faça seu código aqui!
idade = int(input("qual eh a sua idade: "))

if idade < 12:
	taxa = 20 + 1.25
	print(round(taxa, 2))
elif idade == 12:
	taxa = 20 + 2.25
	print(round(taxa, 2))
else:
	taxa = 20 + 3.25
	print(round(taxa, 2))