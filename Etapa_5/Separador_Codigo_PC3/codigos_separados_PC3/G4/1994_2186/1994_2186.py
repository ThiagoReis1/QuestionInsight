amino=input("qual o aminoacido: ").lower()
o=15.9994
c=12.011
n=14.00674
h=1.0079

if(amino=="histidina"):
	x=c*6+h*10+n*3+o*2
	print(round(x,2))
elif(amino=="leucina"):
	x=c*6+h*13+n+o*2
	print(round(x,2))
elif(amino=="lisina"):
	x=c*6+h*15+n*2+o*2
	print(round(x,2))
else:
	print("Entrada:",amino)
	print("Dado Invalido")