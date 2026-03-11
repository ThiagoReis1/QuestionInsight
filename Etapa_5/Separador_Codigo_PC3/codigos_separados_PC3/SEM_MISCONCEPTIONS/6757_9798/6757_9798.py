# faça seu código aqui!
n = int(input("numero de pizzas encomendadas: "))

if n<3:
	total = (n * 5) + 3.0
elif n == 3:
	total = (n * 5) + 3.25
else:
	total = (n * 5) + 4.50
	
print(round(total, 2))