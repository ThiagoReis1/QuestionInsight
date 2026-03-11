# faça seu código aqui!
horas = float(input("Digite o tempo de permanencia do veiculo: "))

if horas < 2:
	total = 5.00 + 1.25
	print(round(total,2))
elif horas == 2:
	total = 5.00 + 2.25
	print(round(total,2))
else:
	total = 5.00 + 3.25
	print(round(total,2))