tempo = int(input("Tempo:"))
if (tempo>=0)and(tempo<=100):
	pulv = 80.00
	piloto = 3000.00
	valor_total =(tempo*pulv)+(piloto)
	print(round((valor_total),2))
elif (tempo>100)and(tempo<=200):
	pulv = 90.00
	piloto = 4000.00
	valor_total =(tempo*pulv)+(piloto)
	print(round((valor_total),2))
elif (tempo>200)and(tempo<=300):
	pulv = 100.00
	piloto = 5000.00
	valor_total =(tempo*pulv)+(piloto)
	print(round((valor_total),2))
elif (tempo>300):
	pulv = 110.00
	piloto = 6000.00
	valor_total =(tempo*pulv)+(piloto)
	print(round((valor_total),2))
else:
	print("erro")