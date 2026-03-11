# faça seu código aqui!
a = int(input("numero de pizzas: "))

if a == 3:
	a1 = a * 5.00 + 3.25
	print(round(a1,2))
	
elif a < 3:
	a2 = a * 5.00 + 3.00
	print(round(a2,2))
	
else:
	a3 = a * 5.00 + 4.50
	print(round(a3,2))
	