nome=input("Digite o tipo de aminoacido: ")
o=15.999
c=12.011
n=14.00674
h=1.00794

gluta=(c*5+h*8+n*1+o*4)
hist=(c*6+h*10+n*3+o*2)
prol=(c*5+h*10+n+o*2)

if(nome.lower()=="glutamina"):
	peso=round(gluta,2)
	print(peso)
elif(nome.lower()=="histidina"):
	peso=round(hist,2)
	print(peso)
elif(nome.lower()=="prolina"):
	peso=round(prol,2)
	print(peso)
else:
	print("Entrada: ",nome)
	print("Dado Invalido")
