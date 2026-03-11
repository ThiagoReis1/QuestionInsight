n = input("Nome do Amino-ácido:").upper()
O = 15.9994
C = 12.011
N = 14.00674
H = 1.0079

if(n!="GLICINA")and(n!="PROLINA")and(n!="SERINA"):
	print("Entrada:",n)
	print("Dado Invalido")
elif n=="GLICINA":
	p = (C*2)+(H*5)+N+(O*2)
	print(round(p,2))
elif(n=="PROLINA"):
	p = (C*5)+(H*10)+N+(O*2)
	print(round(p,2))
else:
	p = (C*3)+(H*7)+N+(O*3)
	print(round(p,2))