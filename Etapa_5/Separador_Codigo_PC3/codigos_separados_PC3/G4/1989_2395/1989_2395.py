n = input()

if(n.upper()=="ASPARAGINA"):
	p = (4*12.011) + (8*1.00794) + (2*14.00674) + (3*15.999)
	print(round(p, 2))
elif(n.upper()=="GLUTAMINA"):
	p = (5*12.011) + (8*1.00794) + (1*14.00674) + (4*15.999)
	print(round(p, 2))
elif(n.upper()=="TRIPTOFANO"):
	p = (11*12.011) + (11*1.00794) + (2*14.00674) + (2*15.999)
	print(round(p, 2))
else:
	print("Entrada:", n)
	print("Dado Invalido")