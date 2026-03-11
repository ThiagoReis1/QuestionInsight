nome=input("entre com aminoacido glicina ou serina : ")

O=15.9994
C=12.011
N=14.00674
H=1.0079


if (nome.upper()=="GLICINA"):
	calc =C*2+H*5+N+O*2
else:
	calc=C*3+H*7+N+O*3

print(round(calc,2))
	