medida = input("A unidade esta em B ou W? ")
vm = float(input("Digite o valor da medida: "))

if(medida.upper() == "W"):
	total = 3.41214 * vm
	
else:
	total = vm / 3.41214
	
print(round(total,2))