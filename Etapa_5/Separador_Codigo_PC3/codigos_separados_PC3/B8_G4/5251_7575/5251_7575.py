c=input("cidade destino: ")
i=int(input("idade do passageiro: "))


PV=500.0
STR=370.0
BLM=600.0
TF=360.0
TB=550.0

if((c!= "porto velho") and (c!="santarem") and (c!="belem") and (c!="tefe") and (c!="tabatinga") or (i<0) or (i>150)):
	print("Entradas invalidas")
elif(c=="porto Velho"):
	if((i>=0) and (i <=2)):
		valor=PV*0
		print("Passagem: R$", round(valor,2))
	elif((i>2) and (i<=12)):
		valor=PV/2
		print("Passagem: R$", round(valor,2))
	elif((i>=65) and (i<=150)):
		valor=PV-(PV*0.3)
		print("Passagem: R$", round(valor,2))
	else: print("Passagem: R$", round(PV,2))
elif(c=="santarem"):
	if((i>=0) and (i<=2)):
		valor=STR*0
		print("Passagem: R$", round(valor,2))
	elif((i>2) and (i<=12)):
		valor=STR/2
		print("Passagem: R$", round(valor,2))
	elif((i>=65) and (i<=150)):
		valor=STR-(STR*0.3)
		print("Passagem: R$", round(valor,2))
	else:
		print("Passagem: R$", round(STR,2))
elif(c=="belem"):
	if((i>=0) and (i<=2)):
		valor=BLM*0
		print("Passagem R$", round(valor,2))
	elif((i>2) and (i<=12)):
		valor=BLM/2
		print("Passagem: R$", round(valor,2))
	elif((i>=65) and (i<=150)):
		valor=BLM-(BLM*0.3)
		print("Passagem: R$", round(valor,2))
	else:
		print("Passagem: R$", round(BLM,2))
elif(c=="tefe"):
	if((i>=0) and (i<=2)):
		valor=TF*0
		print("Passagem: R$", round(valor,2))
	elif((i>2) and (i<=12)):
		valor=TF/2
		print("Passagem: R$", round(valor,2))
	elif((i>65) and(i<=150)):
		valor=TF-(TF*0.3)
		print("Passagem: R$", round(valor,2))
	else:
		print("Passagem: R$", round(TF,2))
elif(c=="tabatinga"):
	if((i>=0) and (i<=2)):
		valor=TB*0
		print("Passagem: R$", round(valor,2))
	elif((i>2) and (i<=12)):
		valor=TB/2
		print("Passagem: R$", round(valor,2))
	elif((i>65) and (i<=150)):
		valor= TB-(TB*0.3)
		print("Passagem: R$", round(valor,2))
	else:
		print("passagem: R$", round(TB,2))
		
		