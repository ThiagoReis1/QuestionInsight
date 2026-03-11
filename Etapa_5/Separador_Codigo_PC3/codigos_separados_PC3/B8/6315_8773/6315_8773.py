from numpy import*
r= input("").upper()
i=0
cont=0
cont1=0
cont2=0
cont3=0
while i<len(r):
	if r[i]=="I":
		cont= cont+3.75
		cont1= cont1+1
	elif r[i]=="M":
		cont= cont+4.50
		cont2= cont2+1
	elif r[i]=="S":
		cont= cont+2.90
		cont3= cont3+1
	i= i+1
	R= round(cont,2)
print(R,cont1,cont2,cont3)