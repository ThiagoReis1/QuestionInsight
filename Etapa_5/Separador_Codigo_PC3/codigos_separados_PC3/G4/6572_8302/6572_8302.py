# faça seu código aqui!

n = int(input("numero de pizzas: "))

if n < 3:
	vt = (n * 5) + 3
	
elif n > 3:
	vt = 4.50 + (n * 5)

else:
	vt = ( n * 5) + 3.25

print("total=", vt)