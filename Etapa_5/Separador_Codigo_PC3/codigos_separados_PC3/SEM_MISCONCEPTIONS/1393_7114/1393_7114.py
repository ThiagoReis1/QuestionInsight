peso = float(input("Digite o peso da encomenda: "))

form1 = peso * 0.05
form2 = (peso * 0.04) + 60.00

if peso < 5000:
	print(round(form1, 2))
else:
	print(round(form2, 2))