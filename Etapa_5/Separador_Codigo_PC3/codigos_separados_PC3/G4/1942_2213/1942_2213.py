texto= input("qual o nome: ")

O= 15.999
C= 12.011
N= 14.00674
H= 1.00794

if(texto.lower()=="prolina"):
	peso=C*6+H*10+N*3+O*2

else:
	peso=C*5+H*10+N+O*2
	
print(round(peso,2))