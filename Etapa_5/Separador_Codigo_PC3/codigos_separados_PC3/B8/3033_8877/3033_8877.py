x = float(input("Informe um valor para x: "))

if x < -100 or x == 0 or x > 100:
	print("entrada invalida")
	
else: 
	if x >= -100 and x < 0:
		valor = -1 / x
		print(round(valor, 4))
	
	elif x > 0 and x <= 100:
		valor = 1 / x
		print(round(valor, 4))