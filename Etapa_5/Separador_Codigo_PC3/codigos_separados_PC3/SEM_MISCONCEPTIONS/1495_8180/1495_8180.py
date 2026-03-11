x = int(input(": "))

if(x >= 0 and x <= 10000):
	valor = ((x) * 6.0 + 100.0)
	print(round(valor, 2))
elif(x <= 10000 and x >= 20000):
	valor2 = (x * 5.5 + 150.0)
	print(round(valor2, 2))
elif(x <= 20000 and x >= 30000):
	valor3 = ((x) * 5.0 + 200.0)
	print(round(valor3, 2))
else:
	valor4 = ((x) * 4.5 + 250.0)
	print(round(valor4, 2))