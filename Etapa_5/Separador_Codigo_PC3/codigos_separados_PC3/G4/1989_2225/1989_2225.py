x= input("Aminoacido: ").upper()
c=12.011
h=1.00794
o=15.999
n=14.00674

if(x=="ASPARAGINA"):
	x=c*4+h*8+n*2+o*3
	print(round(x,2))
elif(x=="GLUTAMINA"):
	x=c*5+h*8+n*1+o*4
	print(round(x,2))
elif(x=="TRIPTOFANO"):
	x=c*11+h*11+n*2+o*2
	print(round(x,2))
else:
	print("Entrada:",x)
	print("Dado Invalido")