from numpy import*

vet=array(eval(input()))
tot=sum(vet)
cont=0
for i in vet:
	if i > 80.0:
		cont=cont+1
		
print(round(tot-(cont*5.0),2))