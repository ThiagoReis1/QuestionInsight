O= 15.9994
C=12.011
N= 14.00674
H=1.0079
nome= input("Digite o nome do aminoacido: ").upper()
if(nome=="GLICINA"):
	a=C*2+H*5+N+O*2
	print(round(a,2))
elif(nome=="PROLINA"):
	b=C*5+H*10+N+O*2
	print(round(b,2))
elif(nome=="SERINA"):
	c=C*3+H*7+N+O*3
	print(round(c,2))
else:
	print("Entrada: ",nome)
	print("Dado Invalido")
		
