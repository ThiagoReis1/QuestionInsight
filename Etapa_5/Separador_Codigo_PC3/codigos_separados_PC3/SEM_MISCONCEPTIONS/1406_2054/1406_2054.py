ataque = input("tipo de ataque: ")
d4 = int(input("valor N sorteado do dado de quatro faces: "))
t = int(input("numero de turno: "))

if(ataque == "cauda"):
	pt = int(d4/t)
	print(pt)
	
else:
	if(ataque == "cuspe"):
		pt = int((2*d4)/t)
	   print(pt)