peso = float(input("Peso do pacote: "))

taxa = 10

if peso < 5:
	var = taxa + 3.75
	
elif peso > 5:
	var = taxa + 5.75
	
else:
	var = taxa + 4.75
	
print("total=",round(var,2))