# faça seu código aqui!
n = int(input("numero de pizzas emcomendadas: "))

if (n < 3):
	valor = n * 5 + 3
elif (n == 3):
	valor = n * 5 + 3.25
else:
	valor = n * 5 + 4.50

print("total=", round(valor, 2))
	