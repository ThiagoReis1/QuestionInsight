face=int(input("face do dado: "))
cont=0
cont2=0
while(face!=-1 and 1<=face<=10):
	cont=cont+1
	if(face==5):
		cont2=cont2+1
	face=int(input("face do dado: "))	
print(cont)
print(round((cont2/cont)*100, 2))
