x=str(input("x?"))
y=int(input("y?"))

p1=500.0
p2=370.0
p3=600.0
p4=360.0
p5=550.0

print("Entradas:",x,",",y)

if(x.upper()=="PORTO VELHO")or(x.upper()=="SANTAREM")or(x.upper()=="BELEM")or(x.upper()=="TEFE")or(x.upper()=="TABATINGA"):
	if(x.upper()=="PORTO VELHO"):
		if(y<=2):
			p=0
			print("Passagem: R$",round(p,2))
		elif(2<y<=12):
			p=p1
			p=p/2
			print("Passagem: R$",round(p,2))
		elif(12<y<=64):
			p=p1
			print("Passagem: R$",round(p,2))
		elif(64<y<=150):
			p=p1*0.7
			print("Passagem: R$",round(p,2))
		elif(y>150):
			print("entradas invalidas")
	elif(x.upper()=="SANTAREM"):
		if(y<=2):
			p=0
			print("Passagem: R$",round(p,2))
		elif(2<y<=12):
			p=p2
			p=p/2
			print("Passagem: R$",round(p,2))
		elif(12<y<=64):
			p=p2
			print("Passagem: R$",round(p,2))
		elif(64<y<=150):
			p=p2*0.7
			print("Passagem: R$",round(p,2))
		elif(y>150):
			print("entradas invalidas")
	elif(x.upper()=="BELEM"):
		if(y<=2):
			p=0
			print("Passagem: R$",round(p,2))
		elif(2<y<=12):
			p=p3
			p=p/2
			print("Passagem: R$",round(p,2))
		elif(12<y<=64):
			p=p3
			print("Passagem: R$",round(p,2))
		elif(64<y<=150):
			p=p3*0.7
			print("Passagem: R$",round(p,2))
		elif(y>150):
			print("entradas invalidas")
	elif(x.upper()=="TEFE"):
		if(y<=2):
			p=0
			print("Passagem: R$",round(p,2))
		elif(2<y<=12):
			p=p4
			p=p/2
			print("Passagem: R$",round(p,2))
		elif(12<y<=64):
			p=p4
			print("Passagem: R$",round(p,2))
		elif(64<y<=150):
			p=p4*0.7
			print("Passagem: R$",round(p,2))
		elif(y>150):
			print("entradas invalidas")
	elif(x.upper()=="TABATINGA"):
		if(y<=2):
			p=0
			print("Passagem: R$",round(p,2))
		elif(2<y<=12):
			p=p5
			p=p/2
			print("Passagem: R$",round(p,2))
		elif(12<y<=64):
			p=p5
			print("Passagem: R$",round(p,2))
		elif(64<y<=150):
			p=p5*0.7
			print("Passagem: R$",round(p,2))
		elif(y>150):
			print("entradas invalidas")
else:
	print("entradas invalidas")
