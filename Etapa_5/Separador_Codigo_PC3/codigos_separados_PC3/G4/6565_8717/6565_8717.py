# faça seu código aqui!
a = int(input("Distancia de entrega: "))

if a < 10:
	r = 50 + 5.50
	print("total=", round(r, 2))
elif a == 10:
	r = 50 + 7.75
	print("total=", round(r, 2))
else:
	r = 50 + 10.00
	print("total=", round(r, 2))