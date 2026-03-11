energia = float(input("Informe o valor de seu consumo em  kWh: "))
tarifa = 0
taxa_iluminacao = 0
	
if (energia <= 150):
	tarifa = 0.60
	taxa_iluminacao = 5.00
elif (energia >= 150 and energia <= 250):
	tarifa = 0.65
	taxa_iluminacao = 8.00
elif (energia >= 250 and energia <= 350):
	tarifa = 0.70
	taxa_iluminacao = 12.00
else: 
	tarifa = 0.75
	taxa_iluminacao = 16.00
	
valor = (energia * tarifa) + taxa_iluminacao
print(round(valor, 2))
