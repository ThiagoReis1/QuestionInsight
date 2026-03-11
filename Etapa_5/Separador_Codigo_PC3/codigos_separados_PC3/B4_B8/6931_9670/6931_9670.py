vlr= float(input("valor da compra: ")) 
oppag= input("forma de pagamento: ").upper()

if oppag == "C":
	parcela= int(input("quantas vezes? "))
	if parcela == 2:
		j= vlr + vlr*0.07
		print(round(j,2))
	else:
		j= vlr
		print(j)
elif oppag == "P":
	dct= vlr - vlr*0.18
	print(round(dct, 2))
elif oppag == "D":
	dct= vlr - vlr*0.18	
	print(round(dct, 2))



