d= input("Qual o destino?")
i= int(input("Qual a idade?"))

print("Entradas:",d,",",i)
if (d!= "Porto Velho") or (d!= "Santarem") or (d!="Belem") or (d!="Tefe") or (d!="Tabatinga"):
	s="entradas invalidas"
if (i<0) or (i>150):
	s="entradas infalidas"
if (i<=2):
	if (d=="Porto Velho"):
		s=0
	elif (d=="Santarem"):
		s=0
	elif (d=="Belem"):
		s=0
	elif (d=="Tefe"):
		s=0
	elif (d=="Tabatinga"):
		s=0
if (i>=3) or (i<=12):
	if (d=="Porto Velho"):
		s= 500/2
	elif (d=="Santarem"):
		s= 370/2
	elif (d=="Belem"):
		s= 600/2
	elif (d=="Tefe"):
		s= 360/2
	elif (d=="Tabatinga"):
		s= 550/2
if (i>=65):
	if(d=="Porto Velho"):
		s= 500 - (500*0.3)
	elif (d=="Santarem"):
		s= 370 - (360*0.3)
	elif (d=="Belem"):
		s = 600 - (600*0.3)
	elif (d=="Tefe"):
		s = 360 - 360*0.3
	elif (d=="Tabatinga"):
		s= 550 - (550*0.3)
print("Passagem: R$", round(s,2))