from numpy import*
r=input(" ")
i=0
cont=0
cont1=0
cont2=0
cont3=0
while i<len(r):
	if r[i] == "B":
		cont=cont+3.75
		cont1=cont1+1
	elif r[i] == "C":
		cont=cont+7.90
		cont2=cont2+1
	elif r[i] == "E":
		cont=cont+9.85
		cont3=cont3+1
	i= i+1
x = round(cont, 2)
print(x,cont1,cont2,cont3)