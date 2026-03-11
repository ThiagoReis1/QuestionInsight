quant = float(input("Quantidade de roupa: "))

if (quant < 10):
	taxa = 3.25

elif (quant > 10):
	taxa = 6

else:
	taxa = 4.5

precofinal = 30 + taxa

print(round(precofinal,2))