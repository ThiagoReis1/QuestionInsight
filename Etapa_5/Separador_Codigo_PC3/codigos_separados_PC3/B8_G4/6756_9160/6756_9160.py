qtd = int(input("Quantidade de dias: "))

if (qtd < 15):
	vt = (175 * qtd) + 20
	print(round(vt, 2))
elif (qtd == 15):
	vt = qtd * 175 + 16
	print(round(vt, 2))
elif (qtd > 15):
	vt = qtd * 175 + 10
	print(round(vt, 2))