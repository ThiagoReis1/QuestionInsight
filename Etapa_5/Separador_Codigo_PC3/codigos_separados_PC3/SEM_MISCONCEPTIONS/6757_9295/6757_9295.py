# faça seu código aqui!
quant = int(input("Insira a quantidade de pizzas: "))

if quant < 3:
	a = 3.00
elif quant == 3:
	a = 3.25
else:
	a = 4.50
b = (quant * 5.00) + a
print(round(b, 2))