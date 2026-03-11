# faça seu código aqui!
ab = 60.0
vel = int(input("Velocidade:"))
if vel<50:
	taxa = ab + 4.50
	print(round(taxa, 2))
elif vel==50:
	taxa = ab + 5.50
	print(round(taxa, 2))
else:
	taxa = ab + 6.50
	print(round(taxa, 2))