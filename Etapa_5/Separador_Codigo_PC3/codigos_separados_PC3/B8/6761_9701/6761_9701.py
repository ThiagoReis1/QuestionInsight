# faça seu código aqui!
tax = float(input("qual a velocidade da sua internet? "))
valor = 60
if tax == 50:
	total = valor + 5.50
	print(round(total, 2))
elif tax < 50:
	total = valor + 4.50
	print(round(total, 2))
elif tax > 50:
	total = valor + 6.50
	print(round(total, 2))