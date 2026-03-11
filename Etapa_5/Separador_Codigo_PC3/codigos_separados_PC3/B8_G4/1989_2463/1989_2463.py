ami=input("AMinoácido: ").upper()
O= 15.999
C= 12.011
N= 14.00674
H= 1.00794

if(ami=="ASPARAGINA" or ami=="GLUTAMINA" or ami=="TRIPTOFANO"):
	if(ami== "ASPARAGINA"):
		a= C*4 + H*8 + N*2 + O*3
		print(round(a,2))
	else:
		if(ami=="GLUTAMINA"):
			b= C*5 + H*8 + N + O*4
			print(round(b,2))
		else:
			if(ami=="TRIPTOFANO"):
				c = C*11 + H*11 + N*2 + O*2
				print(round(c,2))
else:
	print("Entrada:", ami)
	print("Dado Invalido")

