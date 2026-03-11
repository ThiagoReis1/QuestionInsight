nome=input("qual o nome: ").upper()

o=15.9994
c=12.011
n=14.0067
h=1.00794


if(nome=="GLUTAMINA"):
	x=(c*5+h*8+n*1+o*4)
	print(round(x,2))
elif(nome=="SERINA"):
	x=(c*3+h*7+n+o*3)
	print(round(x,2))
elif(nome=="TREONINA"):
	x=(c*4+h*9+n+o*3)
	print(round(x,2))
		
else:	
	print("Entrada:",nome)
	print("Dado Invalido")
		