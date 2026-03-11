nome=input("Digite o nome do aminoácido: ")
o=15.9994
c=12.011
n=14.00674
h=1.0079
if(nome.upper()=="GLICINA"):
	peso=(c*2)+(h*5)+(n*1)+(o*2)
	print(round(peso,2))
else:
	peso=(c*3)+(h*7)+(n*1)+(o*3)
	print(round(peso,2))
	
	
