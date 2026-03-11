dias_alugados = int (input("Digite a quantidade de dias alugados: "))

diaria = 100.0

if (dias_alugados < 7):
	final = (diaria * dias_alugados) + 15
	print (round(final,2))
elif (dias_alugados == 7):
	final = (diaria * dias_alugados) + 12
	print (round(final,2))
elif (dias_alugados > 7):
	final = (diaria * dias_alugados) + 10
	print (round(final,2))