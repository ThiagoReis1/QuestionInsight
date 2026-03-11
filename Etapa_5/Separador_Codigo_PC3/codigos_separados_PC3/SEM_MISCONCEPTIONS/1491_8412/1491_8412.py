peso = int(input("insira o peso: "))
tarifa = float(input("insira a tarifa: "))
taxa = float(input("insira a taxa: "))
if peso >= 0:
	valor = ((peso * tarifa) + taxa)
print(round(valor, 2)