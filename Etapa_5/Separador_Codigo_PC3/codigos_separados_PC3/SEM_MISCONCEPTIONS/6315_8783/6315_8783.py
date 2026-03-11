from numpy import *
prod=input("insira o produto:").upper()
i=0
total=0
cont1=0
cont2=0
cont3=0
while i<len(prod):
	if prod[i]=="I":
		total+=3.75
		cont1+=1
	if prod[i]=="M":
		total+=4.50
		cont2+=1
	if prod[i]=="S":
		total+=2.90
		cont3+=1
	i=i+1
print(round(total,2),cont1,cont2,cont3)