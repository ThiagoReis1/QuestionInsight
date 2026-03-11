a = float(input("Digite o valor de area: "))

if a >= 0 and a <= 100 :
	valor = a * 2 + 100
	print(round(valor,2))
	
elif a > 100 and a <= 2500 :
	valor = a * 1.8 + 150
	print(round(valor,2))
	
elif a > 2500 and a <= 10000 :
	valor = a * 1.5 + 200
	print(round(valor,2))
	
else :
	valor = a * 1.2 + 250
	print(round(valor,2))