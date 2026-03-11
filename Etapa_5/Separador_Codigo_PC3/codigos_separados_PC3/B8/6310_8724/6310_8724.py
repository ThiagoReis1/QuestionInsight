from numpy import*

r=input("insira: ")
i=0
cont=0
cont1=0
cont2=0
cont3=0
while i < len(r):
	if r[i] == "M":
		cont = cont+7.25
		cont1 = cont1+1
	elif r[i] == "P":
		cont= cont+4.75
		cont2=cont2+1
	elif r[i] == "R":
		cont = cont+3.50
		cont3=cont3+1
	i = i+1
	
T= round(cont,2)
print(T,cont1,cont2,cont3)