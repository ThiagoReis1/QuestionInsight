from numpy import *
vn=array(input("Nome dos produtos:").upper())
vp=array(eval(input("Quantia:")))
vet=array(["ARROZ","FEIJAO","BIS","MIOJO","FANTA"])

vet[0]=1.25
vet[1]=2.6
vet[2]=1.8
vet[3]=0.85
vet[4]=3.2

i=0
j=size(vp)
total=0

while(j<sum(vp)):
	if(vn=vet[0]):
		preco=vp*v[0]
		total=total+preco
	elif(vn=)
print(round(total,2))