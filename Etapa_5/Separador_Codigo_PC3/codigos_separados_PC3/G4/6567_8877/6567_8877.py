# faça seu código aqui!
vel = int(input("Informe a velocidade de sua banda larda em (mbps): "))

fixo = 60

if vel < 50:
	taxa = 4.5
	valor = fixo + taxa
	print("total= ", round(valor, 2))
elif vel == 50:
	taxa = 5.5
	valor = fixo + taxa

	print("total= ", round(valor, 2))
else: 
	taxa = 6.5
	valor = fixo + taxa
	print("total= ", round(valor, 2 ))