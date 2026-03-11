# faça seu código aqui!
pacote = float(input("qual o peso do pacote?"))
custofx = 10.00

if pacote < 5:
	total = custofx + 3.75
	print(round(total, 2))
elif pacote == 5:
	total = custofx + 4.75
	print(round(total, 2))
elif pacote > 5:
	total = custofx + 5.75
	print(round(total, 2))