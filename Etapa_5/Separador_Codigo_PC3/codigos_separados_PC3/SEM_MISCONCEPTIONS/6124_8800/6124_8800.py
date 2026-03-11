peso = float(input("digite o peso: "))

if (peso >= 3000) and (peso < 3400):
	viagem = peso * 0.8
elif (peso >= 3400) and (peso < 3900):
	viagem = peso * 1.3
elif (peso >= 3900) and (peso < 4100):
	viagem = peso * 2.1
else:
	viagem + peso * 3
print(round(viagem, 1))