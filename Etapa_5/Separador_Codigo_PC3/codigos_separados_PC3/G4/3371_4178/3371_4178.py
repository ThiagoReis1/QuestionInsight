km = input("Digite K ou M:").upper()
vm = float(input("Valor da medida: "))

if km == "M":
	x = 1.60934*vm
else:
	x = vm/1.60934
print(round(x,2))