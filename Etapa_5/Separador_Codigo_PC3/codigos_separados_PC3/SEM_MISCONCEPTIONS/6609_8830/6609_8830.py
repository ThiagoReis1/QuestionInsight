# faça seu código aqui!
negativo = int(input("numero negativo de entrada: "))
if negativo <= 0:
	while negativo <= 0:
		if (negativo % 3 == 0):
			print(negativo)
			negativo = negativo + 3
else:
	while negativo >= 0:
		if (negativo % 3 == 0):
			print(negativo)
			negativo = negativo - 3
print("fim")