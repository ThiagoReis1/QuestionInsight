# faça seu código aqui!
vel = int(input())
fixo = 60

if vel < 50:
	valor = fixo + 4.5
elif vel == 50:
	valor = fixo + 5.5
elif vel > 50:
	valor = fixo + 6.5
print(round(valor, 2))