vez=input("vez: ").upper()
vezes=int(input("vezes: "))

if (not((vez!="CAMPEAO") or (vez!="VICE-CAMPEAO") or (vezes!=5) or (vezes!=4) or (vezes!=3))):
	print("SELECAO NAO IDENTIFICADA")
else:
	if ((vez=="CAMPEAO") and (vezes==5)):
		print("BRASIL")
	else:
		if((vez=="CAMPEAO") and (vezes==4)):
			print("ITALIA")
		else:
			if ((vez=="VICE-CAMPEAO") and (vezes==4)):
				print("ALEMANHA")
			else:
				print("ARGENTINA")

