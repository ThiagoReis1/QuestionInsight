diaria = 100
dias_alugados = int(input("Digite os dias alugados: "))

if dias_alugados < 7:
	total1 = diaria * dias_alugados + 15
	print(round(total1,2 ))
	
elif dias_alugados == 7:
		total2 = diaria * dias_alugados + 12
		print(round(total2,2))
else:
	dias_alugados > 7
	total3 = diaria * dias_alugados + 10
	print(round(total3,2))