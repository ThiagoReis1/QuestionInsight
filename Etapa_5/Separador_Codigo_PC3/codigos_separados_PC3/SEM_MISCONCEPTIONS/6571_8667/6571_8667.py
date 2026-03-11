# faça seu código aqui!
peso = float(input("Digite o peso do pacote: "))

if (peso < 5):
	total = 10.0 + 3.75
	print("total= ", round(total,2))
elif (peso == 5):
	total = 10.0 + 4.75
	print("total= ", round(total,2))
else:
	total = 10.0 + 5.75
	print("total= ", round(total,2))