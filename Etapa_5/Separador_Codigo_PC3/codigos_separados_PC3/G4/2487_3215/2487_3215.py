prato = int(input())
s = int(input())
bebida = int(input())

print("Entradas:", prato,",",s,",",bebida)
if (bebida==1 or bebida==2 or bebida==3 or bebida==4) and (s==1 or s==2 or s==3 or s==4) and (prato==1 or prato==2 or prato==3 or prato==4): 
	if prato==1:
		p = 180
	elif prato==2:
		p = 230
	elif prato==3:
		p = 250
	else:
		p = 350
	if s==1:
		a = 75
	elif s==2:
		a = 110
	elif s==3:
		a = 170
	else:
		a = 200
	if bebida==1:
		b = 20
	elif bebida==2:
		b = 70
	elif bebida==3:
		b = 100
	else:
		b = 65
	w = p + a + b
	print("Calorias:",w,"cal")

else:
	print("Dados invalidos")



	