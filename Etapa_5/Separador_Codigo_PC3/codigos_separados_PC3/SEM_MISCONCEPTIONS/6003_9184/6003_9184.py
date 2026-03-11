cenouras = float(input("Digite o numero de cenouras: "))

if (cenouras >= 5):
	total_cenouras = cenouras * 0.90
	print(round(total_cenouras, 2))

else:
	total_cenouras = cenouras * 1.20
	print(round(total_cenouras, 2))