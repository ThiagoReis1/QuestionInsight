consumo = int(input("Digite o consumo de agua de uma casa (medido em metros cubicos): "))

if (consumo > 0) and (consumo < 10):
	taxa = 2
elif (consumo >= 10) and (consumo < 20):
	taxa = 2.5
elif (consumo >= 20) and (consumo < 40):
	taxa = 2.75
elif (consumo >= 40):
	taxa = 3
else:
	taxa = "dados invalidos"

conta = taxa * consumo + 20

print(round(conta, 2))