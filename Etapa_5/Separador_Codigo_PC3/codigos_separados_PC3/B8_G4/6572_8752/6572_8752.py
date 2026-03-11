# faça seu código aqui!
d = int(input("Quilometro: "))

if (d < 3):
	a = 5 * d + 3
	print("total=", round(a, 2))
elif (d == 3):
	a = 5 * d + 3.25
	print("total=", round(a,2))
elif (d > 3):
	a = 5 * d + 4.50
	print("total=", round(a,2))
	
