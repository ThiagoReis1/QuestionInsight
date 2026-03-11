x = float(input("Valor de X: "))

a = (-(1/x))
b = 1/x

if x >= -100 and x < 0:
	print(round(a, 4))
	
elif x > 0 and x <= 100:
	print(round(b, 4))

else:
	print("entrada invalida")