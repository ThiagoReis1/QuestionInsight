amino=input().upper()

O=15.9994
C=12.011
N=14.00674
H=1.00794
if(amino!="ARGININA")and(amino!="TIROSINA")and(amino!="TRIPTOFANO"):
	print("Entrada: "+amino)
	print("Dado Invalido")
else:
	if(amino=="ARGININA"):
		print(round(C*6+H*15+N*4+O*2,2))
	else:
		if(amino=="TIROSINA"):
			print(round(C*9+H*11+N+O*3,2))
		else:
			if(amino=="TRIPTOFANO"):
				print(round(C*11+H*11+N*2+O*2,2))