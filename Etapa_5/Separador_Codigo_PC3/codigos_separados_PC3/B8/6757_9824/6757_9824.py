# faça seu código aqui!
n = int(input("qtd de pizzas: "))
entrega = 5.0
total = n * entrega 

if n < 3:
	total += 3.00
elif n == 3:
	total += 3.25
elif n > 3:
	total += 4.50
	
print(round(total, 2))
	
	
