#Ex 02

cargah = float(input("Qual a quantidade de horas trabalhadas pelo professor? "))

if ((cargah >= 0) and (cargah <= 10)):
	pagamento = (cargah * 50) + (500)
	print(round(pagamento,2))
elif ((cargah > 10) and (cargah <= 20)):
	pagamento = (cargah * 60) + (600)
	print(round(pagamento,2))
elif ((cargah > 20) and (cargah <= 30)):
	pagamento = (cargah * 70) + (700)
	print(round(pagamento,2))
elif ((cargah > 30)):
	pagamento = (cargah * 80) + (800)
	print(round(pagamento,2))

