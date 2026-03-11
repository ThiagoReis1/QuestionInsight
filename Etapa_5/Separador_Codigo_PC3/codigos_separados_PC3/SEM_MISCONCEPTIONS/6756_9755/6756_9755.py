dia = int(input("digite aqui muleke: "))

valor = 175.00

if dia < 15:
	total = valor * dia + 20.00
	print(total)
	
elif dia == 15:
	total = valor * dia + 16.00
	print(total)
	
else:
	total = valor * dia + 10.00
	print(total)