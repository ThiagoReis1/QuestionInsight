# faça seu código aqui!
qd = int(input("dias de aluguel: "))

diarias = 100

if qd < 7:
	valor_total = diarias * qd + 15.00
	print(round(valor_total,2))
elif qd == 7:
	valor_total = diarias * qd + 12.00
	print(round(valor_total,2))
else:
	valor_total = diarias * qd + 10.00
	print(round(valor_total,2))