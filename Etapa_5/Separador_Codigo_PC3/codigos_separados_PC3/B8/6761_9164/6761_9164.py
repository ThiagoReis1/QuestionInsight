# faça seu código aqui!
vel = float(input("digite a velocidade: "))
valorfixo = 60.00

if vel < 50:
	taxa = 4.50
elif vel == 50:
	taxa = 5.50
elif vel > 50:
	taxa = 6.50

total = valorfixo + taxa
print(round(total, 2))