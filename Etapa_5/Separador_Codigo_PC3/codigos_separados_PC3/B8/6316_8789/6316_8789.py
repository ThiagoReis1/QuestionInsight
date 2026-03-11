from numpy import*

r=input()
i=0
cont=0
cont1=0
cont2=0
cont3=0

while i < len(r):
	if r[i]=="D":
		cont=cont+2.25
		cont1=cont1+1
	elif r [i]=="S":
		cont=cont+4
		cont2=cont2+1
	elif r [i]=="I":
		cont=cont+6.90
		cont3=cont3+1
	i=i+1

t=round(cont,2)
print(t,cont1,cont2,cont3)