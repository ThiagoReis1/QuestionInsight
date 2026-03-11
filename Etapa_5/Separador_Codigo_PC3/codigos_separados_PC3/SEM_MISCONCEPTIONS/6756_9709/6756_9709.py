dias = int(input("digite a quantidade de dias: "))

if dias < 15:
	taxa = 20
else:
	if dias == 15:
		taxa = 16
	else:
		taxa = 10
valor_total = (175 * dias) + taxa

print(round(valor_total, 2))