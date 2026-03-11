consumo = int(input("digite consumo:"))

if consumo <= 150:
	tarifa = 0.60
	taxa_iluminacao = 5.00
elif consumo <= 250:
	tarifa = 0.65
	taxa_iluminacao = 8.00
elif consumo <= 350:
	tarifa = 0.70
	taxa_iluminacao = 12.00
else:
	tarifa = 0.75
	taxa_iluminacao = 16.00
	
valor = consumo * tarifa + taxa_iluminacao

valor_arredondado = round(valor, 2)

print(valor_arredondado)