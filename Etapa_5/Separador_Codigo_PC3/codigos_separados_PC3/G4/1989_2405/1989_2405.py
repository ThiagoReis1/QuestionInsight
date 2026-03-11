aminoacido = input("digite o nome do aminoacido: ")

O = 15.999
C = 12.011
N = 14.00674
H = 1.00794
	
aspa = C*4+H*8+N*2+O*3
glut = C*5+H*8+N*1+O*4
trip = C*11+H*11+N*2+O*2

if(aminoacido.upper()=="ASPARAGINA"):
	print(round(aspa, 2))
	
elif(aminoacido.upper()=="GLUTAMINA"):
	print(round(glut, 2))
	
elif(aminoacido.upper()=="TRIPTOFANO"):
	print(round(trip, 2))
	
else:
	print("Entrada:",aminoacido )
	print("Dado Invalido")