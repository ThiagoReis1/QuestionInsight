aminoacido = input("Nome do aminoacido: ")
O=15.9994
C=12.011
N=14.00674
H=1.00794
if(aminoacido=="alanina".upper()):
	p=3*C+7*H+N+2*O
	print(round(p,2))
elif(aminoacido=="valina".upper()):
	p=5*C+H*11+N+2*O
	print(round(p,2))
elif(aminoacido=="tirosina".upper()):
	p=9*C+11*H+N+3*O
	print(round(p,2))
else:
	print("Entrada: ",aminoacido)
	print("Dado Invalido")
	
	