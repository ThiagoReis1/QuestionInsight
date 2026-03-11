at=input("Tipo de ataque:")
R=int(input("Numero de rodadas: "))
D1=int(input("D1: "))
D2=int(input("D2: "))
p=D1*D2
c=(D1+D2+1)*R
if(at.lower()=="polen"):
	print(p)
else:
	print(c)