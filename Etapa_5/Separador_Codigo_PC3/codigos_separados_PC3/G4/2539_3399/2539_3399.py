x = float(input("valor do premio: "))
y = float(input("saque mensal fixo: "))
z = float(input("taxa de juros: "))

k = x
i = 1

if(x > 0) and (y > 0) and (z > 0):
	while(k < x + x*0.2):
		k = k*z - y
		i = i + 1
		print(round(i, 2))
else:
	print("Dados incorretos")