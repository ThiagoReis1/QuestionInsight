p=int(input("informe o prato: "))
s=int(input("sobremesa: "))
b=int(input("bebida: "))
print("Entradas: ",p,",",s,",",b)
if (p==1 or p==2 or p==3 or p==4) and (s==1 or s==2 or s==3 or s==4) and (b==1 or b==2 or b==3 or b==4):
	if p==1:
		p=180
	elif p==2:
		p=230
	elif p==3:
		p=250
	else:
		p=350
	if s==1:
		s=75
	elif s==2:
		s=110
	elif s==3:
		s=170
	else:
		s=200
	if b==1:
		b=20
	elif b==2:
		b=70
	elif b==3:
		b=100
	else:
		b=65
	print("Calorias: ",(p+s+b),"cal")
else:
	print("Dados invalidos")

	
		
