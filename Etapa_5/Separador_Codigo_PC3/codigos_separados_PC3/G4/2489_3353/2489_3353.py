cid=input("digite a cidade: ")
ida=int(input("digite a idade: "))

if(0<ida<150):
	if(cid=="Porto Velho"):
		pas=500
		if(ida<=2):
			paga=0
	
		elif(3<=ida<=12):
			paga=pas/2
	
		elif(65<=ida):
			paga=pas*0.7
		else:
			paga=pas
		
	elif(cid=="Santarem"):
		pas=370
		if(ida<=2):
			paga=0
	
		elif(3<=ida<=12):
			paga=pas/2
	
		elif(65<=ida):
			paga=pas*0.7
		else:
			paga=pas
	elif(cid=="Belem"):
		pas=600
		if(ida<=2):
			paga=0
	
		elif(3<=ida<=12):
			paga=pas/2
	
		elif(65<=ida):
			paga=pas*0.7
		else:
			paga=pas
		
	elif(cid=="Tefe"):
		pas=360
		if(ida<=2):
			paga=0
	
		elif(3<=ida<=12):
			paga=pas/2
	
		elif(65<=ida):
			paga=pas*0.7
		else:
			paga=pas
	elif(cid=="Tabatinga"):
		pas=550
		if(ida<=2):
			paga=0
	
		elif(3<=ida<=12):
			paga=pas/2
	
		elif(65<=ida):
			paga=pas*0.7
		else:
			paga=pas
	else:
		print("Entradas:", cid,",", ida)
		print("entradas invalidas")
	
	print("Entradas:",cid,",",ida)
	print("Passagem: R$",round(paga,2))
else:
	print("Entradas:", cid,",", ida)
	print("entradas invalidas")
				

