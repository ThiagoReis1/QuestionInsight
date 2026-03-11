nome=input("Entrada:").upper()
o=15.9994
c=12.011
n=14.00674
h=1.0079
if(nome=="GLICINA"):
	pmo=2*c+h*5+n+o*2
	print(round(pmo,2))
elif(nome=="PROLINA"):
	pem=5*c+h*10+n+o*2
	print(round(pem,2))
elif(nome=="SERINA"):
	pml=c*3+h*7+n+o*3
	print(round(pml,2))
else:
	print("Entrada:",nome)
	print("Dado Invalido")
	