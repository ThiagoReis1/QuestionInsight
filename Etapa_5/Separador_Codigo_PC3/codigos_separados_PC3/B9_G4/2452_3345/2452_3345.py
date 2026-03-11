p = float(input("Peso: "))
h = float(input("Altura: "))
imc = p / (h**2)

if (imc < 18.5):
	m = "abaixo do peso"
elif (imc >= 18.5) and (imc < 25):
	m = "normal"
elif (imc >= 25) and (imc <30):
	m = "acima do peso"
else:
	m = "obeso"
print(m)