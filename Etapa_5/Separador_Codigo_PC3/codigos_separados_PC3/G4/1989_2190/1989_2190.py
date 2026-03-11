nome=input("Nome do aminoacido:").upper()

O=15.999
C=12.011
N=14.00674
H=1.00794
if(nome == "ASPARAGINA"):
	A=(C*4+H*8+N*2+O*3)
	print(round(A,2))	
elif(nome == "GLUTAMINA"):
	G=(C*5+H*8+N*1+O*4)
	print(round(G,2))
elif(nome == "TRIPTOFANO"):
	T=(C*11+H*11+N*2+O*2)
	print(round(T,2))		
else:
	print("Entrada: %s" %(nome))		
	print("Dado Invalido")		