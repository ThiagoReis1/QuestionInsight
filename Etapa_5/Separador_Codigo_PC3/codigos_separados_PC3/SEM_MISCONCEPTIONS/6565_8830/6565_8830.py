distancia_km = int(input("frete inovador! coloque a distancia em km da nossa empresa para a sua casa (utiliza apenas numeros): "))
custo_inicial = 50.00

if distancia_km == 10:
	taxa = 7.75
	total = taxa + custo_inicial
	print("total=", round(total,2))
elif distancia_km <= 10:
	taxa = 5.50
	total = taxa + custo_inicial
	print("total=", round(total,2))
else:
	taxa = 10.00
	total = taxa + custo_inicial
	print("total=", round(total,2))
	


