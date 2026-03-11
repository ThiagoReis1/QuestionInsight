nome=input("nome do aminoacido: ")

O=15.999
C=12.011
N=14.00674
H=1.00794
aspar= (C*4)+(H*8)+(N*2)+(O*3)
gluta= (C*5)+(H*8)+(N*1)+(O*4)
tript= (C*11)+(H*11)+(N*2)+(O*2)

if(nome.upper()=="ASPARAGINA"):
	peso=round(aspar,2)
	print(peso)
elif(nome.upper()=="GLUTAMINA"):	
	peso=round(gluta,2)
	print(peso)
elif(nome.upper()=="TRIPTOFANO"):	
	peso=round(tript,2)
	print(peso)
else:
	print("Entrada: ",nome)
	print("Dado Invalido")