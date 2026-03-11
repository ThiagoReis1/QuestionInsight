bast = input("Insira o nome do bastardo:")
if (bast=="Snow") or (bast=="Stone") or (bast=="Rivers") or (bast=="Storm") or (bast=="Sand") or (bast=="Pyke") or (bast=="Flowers") or (bast=="Hill") or (bast=="Waters"):
	if bast=="Snow":
		m = "Norte"
	elif bast=="Stone":
		m  = "Vale"
	elif bast=="Rivers":
		m = "Terras Fluviais"
	elif bast =="Storm":
		m = "Terras de Tempestade"
	elif bast == "Sand":
		m = "Dorne"
	elif bast == "Pyke":
		m = "Ilhas de Ferro"
	elif  bast == "Flowers":
		m = "Campina"
	elif bast =="Hill":
		m  ="Terras Ocidentais"
	elif bast=="Waters":
		m = "Terras da Coroa"
	print (m)
else:
	 print("Entrada",bast,"invalida")
