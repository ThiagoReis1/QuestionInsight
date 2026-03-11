#Valor consumido
consumo = float(input("Valor consumido:"))
gorj1 = consumo*0.06
gorj2 = consumo*0.1

#Valor total da compra
if (consumo>300):
	print(round(gorj1+consumo,2))
else:
	print(round(gorj2+consumo,2))
