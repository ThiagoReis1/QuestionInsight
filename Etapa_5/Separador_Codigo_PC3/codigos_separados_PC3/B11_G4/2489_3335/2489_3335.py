c = input("Cidade: ")
i = int(input("Idade: "))

print("Entradas:",c,",",i)

if(i>=0 and i<=150):
	if(c=="Porto Velho"):
		if(i<=2):
			vt=0
		elif(3<=i and i<=12):
			vp=500
			vt= vp/2
		elif(i>=65):
			vp=500
			vt = vp - ((30/100)*vp)
		else:
			vt=500
	elif(c=="Santarem"):
		if(i<=2):
			vt=0
		elif(i>=3 and i<=12):
			vp=370
			vt= vp - ((50/100)*vp) 
		elif(i>=65):
			vp=370
			vt = vp - ((30/100)*vp)
		else:
			vt=370
	elif(c=="Belem"):
		if(i<=2):
			vt=0
		elif(i>=3 and i<=12):
			vp=600
			vt= vp - ((50/100)*vp) 
		elif(i>=65):
			vp=600
			vt = vp - ((30/100)*vp)
		else:
			vt=600
	elif(c=="Tefe"):
		if(i<=2):
			vt=0
		elif(i>=3 and i<=12):
			vp=360
			vt= vp - ((50/100)*vp) 
		elif(i>=65):
			vp=360
			vt = vp - ((30/100)*vp)
		else:
			vt=360
	else:
		if(i<=2):
			vt=0
		elif(i>=3 and i<=12):
			vp=550
			vt= vp - ((50/100)*vp) 
		elif(i>=65):
			vp=550
			vt = vp - ((30/100)*vp)
		else:
			vt=550
	print("Passagem: R$",round(vt,2))
else:
	print("entradas invalidas")





