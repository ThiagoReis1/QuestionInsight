var1 = int(input("Valor: "))

soma = 0

while (var1 != -1):
	if (var1 >= 100 and var1 <=199):
		soma = soma + 1
		
	var1 = int(input("Valor: "))
	
print(soma)