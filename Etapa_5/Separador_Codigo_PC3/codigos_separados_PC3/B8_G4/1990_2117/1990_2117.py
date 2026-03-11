amin=input("nome do aminoácido: ").upper()

O=15.9994
C=12.011
N=14.0067
H=1.00794

if(amin!="GLUTAMINA" and amin!="SERINA" and amin!="TREONINA"):
	print("Entrada:",amin)
	print("Dado Invalido")
elif(amin=="GLUTAMINA"):
	g=C*5+H*8+N*1+O*4
	print(round(g,2))
elif(amin=="SERINA"):
	s=C*3+H*7+N+O*3
	print(round(s,2))
elif(amin=="TREONINA"):
	t=C*4+H*9+N+O*3
	print(round(t,2))