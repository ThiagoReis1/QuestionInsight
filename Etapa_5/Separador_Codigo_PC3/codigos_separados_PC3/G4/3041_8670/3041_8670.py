x = float(input("Digite um numero: "))

if (x >= -1000) and (x < -2):
	v = -1 / (x + 2)
	print(round(v, 4))
	
elif (x > 2) and (x <= 1000):
	v = 1 / (x -2)
	print(round(v, 4))
	
else: 
	print("entrada invalida")