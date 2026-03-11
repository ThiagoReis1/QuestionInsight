x = float(input("Digite o valor de x: "))
if x<=1:
	resultado = 1
elif 1 < x <=2:
		resultado = 2
elif 2 < x <=3:
		resultado = x ** 2
else:
	resultado= x ** 3

print(round(resultado,2))
	