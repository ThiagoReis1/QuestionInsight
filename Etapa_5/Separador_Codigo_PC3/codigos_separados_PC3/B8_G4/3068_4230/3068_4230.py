nome=input("").upper()
D=int(input())
d1=int(input())
d2=int(input())
S= d1+d2
if(d1<1 or d1>10 or d2<1 or d2>10 or D<0):
	print("Entrada invalida")
elif(nome=="CIMITARRA"):
	dano=2*S + 2*D
	print(dano)
elif(nome=="KATANA"):
	dano=2*S + D
	print(dano)
elif(nome=="SABRE"):
	dano=S+2*D
	print(dano)