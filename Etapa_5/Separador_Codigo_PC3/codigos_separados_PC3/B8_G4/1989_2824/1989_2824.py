a= input("Nome do amioacido:").upper()
if((a =="ASPARAGINA") or (a =="GLUTAMINA") or (a =="TRIPTOFANO")) :
	if(a =="ASPARAGINA"):
		ot=((3*15.999) + (4*12.011) + (2*14.00674) + (8*1.00794))
		print(round(ot, 2))
	elif((a.upper()=="GLUTAMINA")):
		gl= ((5*12.011) + (8*1.00794) + (1*14.00674) and(4*15.999))
		print(round(gl, 2))
	elif((a.upper()=="TRIPTOFANO")):
		tri= ((11*12.011) + (11*1.00794) + (2*14.00674) and(2*15.999))
		print(round(tri,2))
else:
	print("Entrada:", a)
	print("Dado invalido")
		