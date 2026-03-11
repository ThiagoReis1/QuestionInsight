# faça seu código aqui!
qtddias = int(input("Quantos dias?"))

if qtddias <15:
	valortotal = qtddias * 175 + 20
	print(round(valortotal,2))
elif qtddias == 15:
	valortotal = qtddias * 175 + 16
	print(round(valortotal,2))
else:
	valortotal = qtddias * 175 + 10
	print(round(valortotal,2))