# faça seu código aqui!

p = int(input("Informe o numero de pizzas: "))

if (p < 3):
	v = (p * 5) + 3
	print("total=", round(v, 2))
	
elif (p == 3):
	v = (p * 5) + 3.25
	print("total=", round(v, 2))
	
elif (p > 3):
	v = (p * 5) + 4.50
	print("total=", round(v, 2))
	
