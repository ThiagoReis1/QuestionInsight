TA=input("Informe o tipo de Ataque: ")
NR=int(input("Informe o numero de rodadas:"))
V1=int(input("Informe o numero sorteado D1:"))
V2=int(input("Informe o numero sorteado D2:"))
if (TA=="polen"):
	D=V1*V2
else:
	D=NR*((V1+V2)+1)
	
print(D)