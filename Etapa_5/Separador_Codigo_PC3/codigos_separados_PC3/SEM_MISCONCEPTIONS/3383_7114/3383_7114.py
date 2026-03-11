uni = input("Digite em que unidade de medida esta. L para libras ou K para quilogramas: ")
med = float(input("Digite o valor da medida: "))

if uni.upper() == "K":
	form1 = 2.20462 * med
	print(round(form1, 2))
else:
	form2 = med / 2.20462
	print(round(form2, 2))