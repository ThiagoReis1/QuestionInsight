a=input("digite o nome aminoacido: ")
o=15.999
c=12.011
n=14.00674
h=1.00794
if(a.lower()=="glutamina"):
	a1=c*5+h*8+n*1+o*4
	print(round(a1,2))
elif(a.lower()=="histidina"):
	a2=c*6+h*10+n*3+o*2
	print(round(a2,2))
elif(a.lower()=="prolina"):
	a3=c*5+h*10+n*1+o*2
	print(round(a3,2))
else:
	print("Entrada: ",a)
	print("Dado Invalido")
