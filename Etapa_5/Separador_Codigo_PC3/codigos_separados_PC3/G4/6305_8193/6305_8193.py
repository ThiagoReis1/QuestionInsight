v = input("").upper()
cont = 0
cont1 = 0
cont2 = 0
h = 0
l = 0
e = 0 

i = 0
while (i<len(v)):
	if (v[i]=="H"):
		cont=cont+3.85	
		h = h+1
	if (v[i]=="L"):
		cont1 = cont1+2.95
		l = l+1
	if (v[i]=="E"):
		cont2 = cont2+7.90
		e = e+1
	i = i+1

print(round(cont+cont1+cont2, 2),h,l,e)
