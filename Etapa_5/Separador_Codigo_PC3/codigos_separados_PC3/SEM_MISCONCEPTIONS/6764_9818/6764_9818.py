# faça seu código aqui!

fixo = 10.00
pacote = float(input("Peso do pacote: "))

if pacote == 5.00:
	total = fixo + 4.75
elif pacote > 5.00:
	total = fixo + 5.75
else:
	total = fixo + 3.75

print(round(total, 2))