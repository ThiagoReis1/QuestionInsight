consumo_do_plano=float(input("valor do consumo:"))

tarifa_min=1.20
taxa_fixa=25.00+consumo_do_plano*1.40
if(consumo_do_plano<=100):
	valor=tarifa_min*consumo_do_plano
else:
	valor=taxa_fixa
print(round(valor,2))