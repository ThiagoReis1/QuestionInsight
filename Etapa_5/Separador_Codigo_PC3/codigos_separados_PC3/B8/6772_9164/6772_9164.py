valor = float(input("Digite o valor: "))
cod = input("codigo da compra: ")

if cod.upper() == "D" or cod.upper() == "P":
	desc = 0.17
	total = valor - desc * (valor)
elif cod.upper() == "C1":
	desc = 0.00
	total = valor + desc * (valor)
elif cod.upper() == "C2":
	desc = 0.08
	total = valor + desc * (valor)
					
print(round(total, 2))