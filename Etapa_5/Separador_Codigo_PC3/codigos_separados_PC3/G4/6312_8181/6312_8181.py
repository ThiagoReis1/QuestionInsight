s = input("B,C,E: ")
i= 0
cont = 0
cont1= 0
cont2 = 0
vt = 0
B = 3.75
C = 7.90
E = 9.85
tam = len(s)

while (i<tam):
	if(s[i]=="B"):
		cont= cont+1
		vt= vt+B
	if(s[i]=="C"):
		cont1= cont1+1
		vt= vt+C
	if(s[i]=="E"):
		cont2= cont2+1
		vt= vt+E
	i=i+1
print(round(vt,2),cont,cont1,cont2)
		

